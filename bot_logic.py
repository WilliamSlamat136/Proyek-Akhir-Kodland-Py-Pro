from settings import settings
import discord
from discord.ext import commands
# from utils import get_class
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)
problems = ["1. Pertumbuhan Penduduk dan Urbanisasi: Pertumbuhan populasi Jakarta yang pesat, baik dari migrasi internal maupun pertumbuhan alami, menyebabkan peningkatan jumlah kendaraan dan kebutuhan transportasi.",
            "2. Jumlah Kendaraan yang Berlebihan: Tingginya jumlah kendaraan pribadi, baik mobil maupun sepeda motor, tidak sebanding dengan kapasitas jalan yang ada. Ini mengakibatkan lalu lintas yang padat dan seringkali macet.",
            "3. Infrastruktur yang Terbatas: Infrastruktur jalan di Jakarta sering kali tidak cukup untuk menampung volume kendaraan yang ada. Pembangunan jalan baru seringkali tidak sebanding dengan pertumbuhan jumlah kendaraan.",
            "4. Transportasi Publik yang Belum Optimal: Meskipun telah ada upaya untuk meningkatkan layanan transportasi publik seperti TransJakarta, MRT, dan LRT, namun belum sepenuhnya mampu mengatasi kebutuhan masyarakat dan mengalihkan pengguna kendaraan pribadi ke transportasi umum.",
            "5. Manajemen Lalu Lintas yang Kurang Efektif: Sistem manajemen lalu lintas yang kurang optimal, seperti pengaturan lampu lalu lintas, parkir liar, dan kurangnya disiplin berlalu lintas, juga berkontribusi pada kemacetan.",
            "6. Kawasan Pusat Bisnis yang Padat: Banyaknya kegiatan bisnis dan komersial yang terpusat di daerah tertentu, seperti Sudirman, Thamrin, dan Kuningan, menyebabkan konsentrasi kendaraan di kawasan-kawasan tersebut, terutama pada jam-jam sibuk.",
            "7. Perilaku Pengemudi: Perilaku pengemudi yang kurang disiplin, seperti berhenti sembarangan, melanggar rambu lalu lintas, dan tidak mematuhi aturan jalan, memperparah kondisi kemacetan."]

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hai! Saya adalah bot {bot.user}!')

@bot.command()
async def problem(ctx):
    await ctx.send(f'Kemacetan di Jakarta adalah salah satu masalah perkotaan yang paling menonjol dan kompleks.')
    await ctx.send(f'Beberapa faktor yang berkontribusi terhadap masalah ini termasuk:')  
    for problem in problems:
        await ctx.send(problem)

bot.run(settings["TOKEN"])
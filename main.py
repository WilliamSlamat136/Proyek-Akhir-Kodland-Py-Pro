from settings import settings
import discord
from bot_logic import *

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)
problems = ["1. Pertumbuhan Penduduk dan Urbanisasi: Pertumbuhan populasi Jakarta yang pesat, baik dari migrasi internal maupun pertumbuhan alami, menyebabkan peningkatan jumlah kendaraan dan kebutuhan transportasi.",
            "2. Jumlah Kendaraan yang Berlebihan: Tingginya jumlah kendaraan pribadi, baik mobil maupun sepeda motor, tidak sebanding dengan kapasitas jalan yang ada. Ini mengakibatkan lalu lintas yang padat dan seringkali macet.",
            "3. Infrastruktur yang Terbatas: Infrastruktur jalan di Jakarta sering kali tidak cukup untuk menampung volume kendaraan yang ada. Pembangunan jalan baru seringkali tidak sebanding dengan pertumbuhan jumlah kendaraan.",
            "4. Transportasi Publik yang Belum Optimal: Meskipun telah ada upaya untuk meningkatkan layanan transportasi publik seperti TransJakarta, MRT, dan LRT, namun belum sepenuhnya mampu mengatasi kebutuhan masyarakat dan mengalihkan pengguna kendaraan pribadi ke transportasi umum.",
            "5. Manajemen Lalu Lintas yang Kurang Efektif: Sistem manajemen lalu lintas yang kurang optimal, seperti pengaturan lampu lalu lintas, parkir liar, dan kurangnya disiplin berlalu lintas, juga berkontribusi pada kemacetan.",
            "6. Kawasan Pusat Bisnis yang Padat: Banyaknya kegiatan bisnis dan komersial yang terpusat di daerah tertentu, seperti Sudirman, Thamrin, dan Kuningan, menyebabkan konsentrasi kendaraan di kawasan-kawasan tersebut, terutama pada jam-jam sibuk.",
            "7. Perilaku Pengemudi: Perilaku pengemudi yang kurang disiplin, seperti berhenti sembarangan, melanggar rambu lalu lintas, dan tidak mematuhi aturan jalan, memperparah kondisi kemacetan."]

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$hello'):
        await message.channel.send(f'Hai! Saya adalah bot {client.user}!')
    elif message.content.startswith('$problems'):
        await message.channel.send(f'Kemacetan di Jakarta adalah salah satu masalah perkotaan yang paling menonjol dan kompleks.')
        await message.channel.send(f'Beberapa faktor yang berkontribusi terhadap masalah ini termasuk:')
        for problem in problems:
            await message.channel.send(problem)


client.run(settings["TOKEN"])


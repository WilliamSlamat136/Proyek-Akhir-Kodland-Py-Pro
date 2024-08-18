from settings import settings
import discord
from discord.ext import commands
# from utils import get_class
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)
masalah = {"Pertumbuhan Penduduk dan Urbanisasi": "Pertumbuhan populasi Jakarta yang pesat, baik dari migrasi internal maupun pertumbuhan alami, menyebabkan peningkatan jumlah kendaraan dan kebutuhan transportasi.",
            "Jumlah Kendaraan yang Berlebihan": "Tingginya jumlah kendaraan pribadi, baik mobil maupun sepeda motor, tidak sebanding dengan kapasitas jalan yang ada. Ini mengakibatkan lalu lintas yang padat dan seringkali macet.",
            "Infrastruktur yang Terbatas": "Infrastruktur jalan di Jakarta sering kali tidak cukup untuk menampung volume kendaraan yang ada. Pembangunan jalan baru seringkali tidak sebanding dengan pertumbuhan jumlah kendaraan.",
            "Transportasi Publik yang Belum Optimal": "Meskipun telah ada upaya untuk meningkatkan layanan transportasi publik seperti TransJakarta, MRT, dan LRT, namun belum sepenuhnya mampu mengatasi kebutuhan masyarakat dan mengalihkan pengguna kendaraan pribadi ke transportasi umum.",
            "Manajemen Lalu Lintas yang Kurang Efektif": "Sistem manajemen lalu lintas yang kurang optimal, seperti pengaturan lampu lalu lintas, parkir liar, dan kurangnya disiplin berlalu lintas, juga berkontribusi pada kemacetan.",
            "Kawasan Pusat Bisnis yang Padat": "Banyaknya kegiatan bisnis dan komersial yang terpusat di daerah tertentu, seperti Sudirman, Thamrin, dan Kuningan, menyebabkan konsentrasi kendaraan di kawasan-kawasan tersebut, terutama pada jam-jam sibuk.",
            "Perilaku Pengemudi": "Perilaku pengemudi yang kurang disiplin, seperti berhenti sembarangan, melanggar rambu lalu lintas, dan tidak mematuhi aturan jalan, memperparah kondisi kemacetan."}

solusi = {"Peningkatan Transportasi Publik": "Meningkatkan jangkauan, kualitas, dan keterjangkauan transportasi publik sehingga masyarakat lebih tertarik untuk beralih dari kendaraan pribadi ke transportasi umum.",
            "Pengembangan Infrastruktur": "Membangun dan memperbaiki infrastruktur jalan, termasuk pembangunan jalan layang, terowongan, dan jalur-jalur alternatif untuk mengurangi kepadatan lalu lintas.",
            "Regulasi Kendaraan Pribadi": "Menerapkan kebijakan pembatasan penggunaan kendaraan pribadi, seperti sistem ganjil-genap, pembatasan usia kendaraan, atau penerapan pajak yang lebih tinggi untuk kendaraan pribadi.",
            "Manajemen Lalu Lintas yang Lebih Baik": "Meningkatkan sistem manajemen lalu lintas, termasuk penggunaan teknologi seperti sistem transportasi cerdas (ITS), pengaturan lampu lalu lintas yang lebih efisien, dan penegakan hukum yang lebih ketat terhadap pelanggaran lalu lintas.",
            "Pengembangan Kawasan Terpadu": "Mengembangkan kawasan-kawasan terpadu di luar pusat kota untuk mendistribusikan kegiatan bisnis, komersial, dan perumahan sehingga mengurangi konsentrasi kendaraan di pusat kota.",
            "Pendidikan dan Kesadaran Masyarakat": "Mengedukasi masyarakat mengenai pentingnya disiplin berlalu lintas dan manfaat menggunakan transportasi umum."}

dampak_kemacetan_jakarta = {
    "Ekonomi": {
        "Produktivitas Menurun": "Kemacetan menyebabkan waktu perjalanan yang lebih lama, mengurangi produktivitas kerja.",
        "Biaya Operasional Meningkat": "Kemacetan meningkatkan biaya operasional perusahaan, terutama dalam bidang logistik.",
        "Kerugian Ekonomi": "Kerugian ekonomi akibat kemacetan mencapai triliunan rupiah per tahun."
    },
    "Sosial": {
        "Stres dan Kualitas Hidup Menurun": "Waktu yang lama di jalan menyebabkan stres dan menurunkan kualitas hidup.",
        "Waktu Bersama Keluarga Berkurang": "Kemacetan mengurangi waktu yang bisa dihabiskan bersama keluarga.",
        "Ketimpangan Sosial": "Kemacetan memperburuk ketimpangan sosial dalam akses mobilitas."
    },
    "Lingkungan": {
        "Pencemaran Udara": "Kemacetan meningkatkan emisi gas buang kendaraan, berkontribusi pada polusi udara.",
        "Pemanasan Global": "Emisi gas rumah kaca dari kendaraan berkontribusi terhadap perubahan iklim.",
        "Kerusakan Lingkungan": "Penggunaan lahan untuk jalan dan parkir mengurangi ruang hijau dan mengganggu ekosistem."
    },
    "Kesehatan": {
        "Penyakit Pernapasan": "Polusi udara akibat kemacetan meningkatkan risiko penyakit pernapasan.",
        "Stres dan Kesehatan Mental": "Stres kronis akibat kemacetan dapat mempengaruhi kesehatan mental dan fisik.",
        "Kurangnya Aktivitas Fisik": "Waktu yang lama di kendaraan menyebabkan kurangnya aktivitas fisik."
    },
    "Mobilitas dan Aksesibilitas": {
        "Mobilitas Terhambat": "Kemacetan menghambat mobilitas dan akses ke layanan penting.",
        "Menurunnya Kepercayaan terhadap Transportasi Publik": "Kemacetan membuat transportasi publik tidak tepat waktu, menurunkan kepercayaan masyarakat."
    }
}

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def test(ctx, *, arg):
    await ctx.send(arg)

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hai! Saya adalah bot {bot.user}!')

@bot.command()
async def problems(ctx):
    await ctx.send('Kemacetan di Jakarta adalah salah satu masalah perkotaan yang paling menonjol dan kompleks.')
    await ctx.send('Beberapa faktor yang berkontribusi terhadap masalah ini termasuk:')  
    for i, (title, description) in enumerate(masalah.items(), start=1):
        await ctx.send(f"{i}. {title}\n   {description}\n")

@bot.command()
async def solutions(ctx):
    await ctx.send('Solusi yang Mungkin untuk Mengatasi Kemacetan di Jakarta:')
    for i, (title, description) in enumerate(solusi.items(), start=1):
        await ctx.send(f"{i}. {title}\n   {description}\n")

@bot.command()
async def cause(ctx):
    await ctx.send('Kemacetan di Jakarta memiliki dampak yang luas dan signifikan, baik dari segi ekonomi, sosial, lingkungan, maupun kesehatan. Berikut beberapa dampak utama dari kemacetan di Jakarta:')
    for kategori, dampak in dampak_kemacetan_jakarta.items():
        await ctx.send(f"{kategori}:")
        for judul, deskripsi in dampak.items():
            await ctx.send(f"  - {judul}: {deskripsi}")

@bot.command()
async def illustration(ctx):
    with open('images/banner.jpeg', 'rb') as f:
        picture = discord.File(f)
        await ctx.send(file=picture)
    await ctx.send("Gambar illustrasi macet di Jakarta.")

@bot.command()
async def bye(ctx):
    await ctx.send('Bye!')  

bot.run(settings["TOKEN"])

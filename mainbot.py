import discord, random, os
from discord.ext import commands
from botlogic import gen_pass
from botlogic import coins
from model import get_class
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def flipkoin(ctx, detik = 1):
    await ctx.send(coins(detik))

@bot.command()
async def createpass(ctx, ):
    await ctx.send(gen_pass(8))

@bot.command()
async def meme(ctx):
    img_name = random.choice(os.listdir('images'))
    with open(f'images/{img_name}', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

@bot.command()
async def ide_sampah(ctx):
    krj_name = random.choice(os.listdir('kerajinan'))
    with open(f'kerajinan/{krj_name}', 'rb') as f:
        picture = discord.File(f)
        f.close()
    await ctx.send(file=picture)

@bot.command()
async def check(ctx):
    if ctx.message.attachments:
        for file in ctx.massage.attachments:
            await file.save(f'./{file.filename}')
            await ctx.send(f'FILE BERHASIL DISIMPAN DENGAN NAMA {file.filename}')
            hasil = get_class('keras_model.h5', 'label.txt', file.filename )

            if hasil[0]== 'Macan Tutul\n' and hasil[1]>= 0.7:
                await ctx.send('INI ADALAH HEWAN MACAN TUTUL')
                await ctx.send("HARIMAU MEMAKAN DAGING Harimau dapat menghabiskan sekitar 18 kg daging dalam sekali makan.")
                await ctx.send("harimau dapat ditemukan di Asia, mulai dari daratan Turki hingga ke Rusia dan Indonesia")
                await ctx.send("Persentase kemiripan {:,.1f}%".format(hasil[1]*100))

            if hasil[1]== 'harimau\n' and hasil[1]>= 0.7:
                await ctx.send('INI ADALAH HEWAN HARIMAU')
                await ctx.send("MACAN TUTUL MEMAKAN DAGING")
                await ctx.send("Mereka dapat ditemukan di timur laut dan sahara Afrika, Asia Tengah, India, dan Tiongkok")
                await ctx.send("Persentase kemiripan {:,.1f}%".format(hasil[1]*100))

            else:
                await ctx.send('GAMBAR TIDAK BISA TER DETEKSI')
    else:
        await ctx.send('ANDA LUPA MENGIRIM GAMBAR!')


bot.run("")

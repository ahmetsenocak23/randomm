import sqlite3
import discord
from discord.ext import commands
from logic import DB_Manager
from config import DATABASE, TOKEN



# Veri tabanı ile bağlantı kuruluyor


intents = discord.Intents.default()
intents.messages = True
intents.message_content = True


bot = commands.Bot(command_prefix='!', intents=intents)
manager = DB_Manager(DATABASE)
@bot.event
async def on_ready():
    print(f'Bot hazır! {bot.user} olarak giriş yapıldı. ')

@bot.event
async def on_ready(): 
    kanal_id = KANAL İD'NİZ BURAYA
    kanal = bot.get_channel(kanal_id)
    if kanal:
        await kanal.send("Mehaba !helpme yazarak komutları öğrenebilirsin =)")
    

@bot.command(name='merhaba')
async def start_command(ctx):
    await ctx.send("Merhaba! ben film seçmenize yardımcı olabilecek bir botum, seçin ve tadını çıkarın =) ")
    
@bot.command(name='helpme')
async def start_command(ctx):
    await ctx.send("Merhaba! **!movie** rastgele film seçmenizi , **!af2013** 2013 sonrası filmlerden rastgele seçmenizi \n **!be2013** se 2013 öncesi filmlerden rastgele seçmenize olanak tanır.")


@bot.command(name='movie')
async def movie_selector(ctx):
    await ctx.send(manager.random_movie()) 

@bot.command(name="af2013")
async def movie_selector_time(ctx):
    await ctx.send(manager.random_movie_time())

@bot.command(name="be2013")
async def movie_selector_time2(ctx):
    await ctx.send(manager.random_movie_time2())
    

    

bot.run(TOKEN)
    

    


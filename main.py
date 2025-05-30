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
    print(f'Bot hazır! {bot.user} olarak giriş yapıldı.')

@bot.command(name='merhaba')
async def start_command(ctx):
    await ctx.send("Merhaba! ben film seçmenize yardımcı olabilecek bir botum seçin ve tadını çıkarın =) ")

@bot.command(name='movie')
async def movie_selector(ctx):
    await ctx.send(manager.random_movie()) 
    

bot.run(TOKEN)
    

    


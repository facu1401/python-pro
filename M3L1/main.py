import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print('We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send('Hola, soy un bot {bot.user}!')
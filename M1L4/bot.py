import discord
from discord.ext import commands
import random

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print('We have logged in as {bot.user}') 

# Comando para saludar
@bot.command()
async def hello(ctx):
    await ctx.send('Hola, soy un bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh=5):
    await ctx.send("he" * count_heh)


@bot.command()
async def talk_godzilla(ctx):
    preguntas = [
        "¿Sabías que Godzilla es conocido como el Rey de los Monstruos?",
        "¿Cuál es tu titan favorito de Godzilla?",
        "Godzilla tiene la capacidad de destruir ciudades con su aliento atómico. ¿Qué opinas de eso?",
        "King Kong luchó contra Godzilla, ¿quién crees que ganaría?"
    ]
    
    respuesta = random.choice(preguntas)
    await ctx.send(respuesta)  


@bot.command()
async def repetir(ctx, *, mensaje: str):  
    await ctx.send(mensaje)



bot.run("")
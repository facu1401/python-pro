import discord
from discord.ext import commands
import random
import os
import requests


intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)
print(os.listdir('images'))

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

@bot.command()
async def mem(ctx):
    img_name = random.choice(os.listdir('images'))
    with open(f'images/{img_name}', 'rb') as f:
        picture = discord.File(f)
        await ctx.send(file=picture)

def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']


@bot.command('duck')
async def duck(ctx):
    '''Una vez que llamamos al comando duck, 
    el programa llama a la función get_duck_image_url'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)



bot.run("")
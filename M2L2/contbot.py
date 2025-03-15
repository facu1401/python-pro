import discord
import random

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)


questions = {
    "¿Qué proceso convierte el CO2 en oxígeno?": "https://cdn.prod.website-files.com/5ff3273633e29c2a7c8b6c80/60c882dbbed95f1d238d95f3_blog_emisiones-de-co2.jpg",
    "¿Qué significa reciclar?": "https://incinerox.com.ec/wp-content/uploads/Como-organizar-mi-reciclaje-1-1920x1024.webp",
    "¿Dónde debes tirar una botella de plástico?": "https://estaticos-cdn.prensaiberica.es/clip/7a769a28-2ba4-46b6-91bd-23f51f2bd6dd_16-9-discover-aspect-ratio_default_0.jpg",
    "¿Qué tipo de residuos va en el contenedor amarillo?": "https://www.ecoembes.com/sites/default/files/2022-10/contenedor_amarillo.jpg",
    "¿Qué significa la flecha en el símbolo de reciclaje?": "https://foodpacservice.com/wp-content/uploads/2023/11/SIMBOLOS-RECICLAJE-1.jpg",
}

@client.event
async def on_ready():
    print(f'Conectado como {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hola, soy tu Bot!')

    elif message.content.lower().startswith('$quiz'):
        question, image_url = random.choice(list(questions.items()))
        await message.channel.send('Pregunta: {question}')
        await message.channel.send(image_url)  


client.run("")


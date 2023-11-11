#Template para que usen con la clase BOT! 

#Importando librerías (se modifica al gusto)
from keras.models import load_model  # TensorFlow is required for Keras to work
from PIL import Image, ImageOps  # Install pillow instead of PIL
import numpy as np
import discord
import requests  #Asegúrese de que tiene instalada la biblioteca requests. Si no es así, ¡instálala con pip install!
from discord.ext import commands
import os
import random

#NO BORRAR 
# La variable intents almacena los privilegios del bot
intents = discord.Intents.default()

# Activar el privilegio de lectura de mensajes
intents.message_content = True

# Crear un bot en la variable cliente y transferirle los privilegios, también se define que el bot funcione con ! 
bot = commands.Bot(command_prefix='!', intents=intents) 

#Para saber si hemos iniciado sesión
@bot.event
async def on_ready():
    print(f"Hemos iniciado sesión como {bot.user}")

def get_class(model_path, labels_path, image_path):
    np.set_printoptions(suppress=True)
    model = load_model(model_path, compile=False)
    class_names = open(labels_path, "r", encoding="utf-8").readlines()
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
    image = Image.open(image_path).convert("RGB")

    size = (224, 224)
    image = ImageOps.fit(image, size, Image.Resampling.LANCZOS)

    image_array = np.asarray(image)

    normalized_image_array = (image_array.astype(np.float32) / 127.5) - 1

    data[0] = normalized_image_array

    prediction = model.predict(data)
    index = np.argmax(prediction)
    class_name = class_names[index]
    confidence_score = prediction[0][index]

    return(class_name[2:], confidence_score)
#Así se hacen los comandos para que el bot opere
@bot.command()  
async def Micomando(ctx):   #De aquí depende el comando, el nombre que se pone aquí es el comando que el bot usará (!Micomando)
    #AQUÍ VA EL FUNCIONAMIENTO DEL BOT, dependiendo de lo que quieran que haga    
    await ctx.send("Hola, funciono!")  #acá es lo que el BOT va a responderte cuando escribas !Micomando
@bot.command()
async def Revisar(ctx):
    if ctx.message.attachments: 
        for attachments in ctx.message.attachments:
            file_name=attachments.filename
            file_url=attachments.url
            
            await attachments.save(f"./{file_name}")
            await ctx.send(f"Guardé tu imagen en ./{file_url}")
            await ctx.send(get_class(model_path="./keras_model.h5", labels_path="labels.txt", image_path=f"./{file_name}") )
    else:
        await ctx.send("Olvidaste subir tu imagen :( ")
 
bot.run("MTExNDYxMTY0MjgzNjIwNTYyMA.GbqzUf.462yKkIt4C5fXA2fSouA6648HK8_-iRT655jP4")

import os
from meet import *      #to import function from meet.py
import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")    #reads and save discord token into system variables

bot = discord.Client()
@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')


@bot.event
async def on_message(message):
    if message.author==bot.user:
        return 
    if 'https://meet.google.com/' in message.content.lower():      #bot searches for sepecific strings in the text sent by the user
        await message.channel.send('Recieved')   #Bot sends message on receiving the link
        sub=message.content
        print(sub)
        meetjoin(sub)
        return sub
bot.run(TOKEN)

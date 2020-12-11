import os
from meet import *
import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
print("Token is" , TOKEN)

bot = discord.Client()
@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')


@bot.event
async def on_message(message):
    if message.author==bot.user:
        return
    if 'https://meet.google.com/' in message.content.lower():
        await message.channel.send('Recieved')
        sub=message.content
        print(sub)
        meetjoin()
bot.run(TOKEN)
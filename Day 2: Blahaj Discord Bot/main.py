import os
import discord
from random import randint
from keeping_alive import keeping_alive

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    message_content = (message.content).lower()
    with open("images/urls.txt",'r') as file:
      url_list = file.readlines()
    meme_random = randint(0,len(url_list)+1)
    URL = url_list[meme_random]
    if message.author == client.user:
        return

    if message_content == '!blahaj':
      embed=discord.Embed(title="Blahaj Meme", color=0x6996AD)
      embed.set_image(url = URL)
      await message.channel.send(embed = embed)

keeping_alive()
client.run(os.environ['TOKEN'])
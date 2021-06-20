import discord
from discord.ext import commands
import os
import random


client = commands.Bot(command_prefix = '>')

file1 = open("songs.txt","r")

list = []
for i in range (0,26):
  list.append(file1.readline())

@client.command()
async def join (ctx):
  if (ctx.author.voice):
    channel = ctx.message.author.voice.channel
    await channel.connect()
  else:
    await ctx.send("sorry")


@client.command(pass_context=True)
async def leave(ctx):
    if ctx.message.author.voice:
        #channel = ctx.message.author.voice.channel
        server = ctx.message.guild.voice_client
        await server.disconnect()


@client.command()
async def ping(ctx):
  for i in range (1,10):
    line = str(random.choice(list))
    await ctx.send(line)

@client.event
async def on_ready():
  print('Bot is ready.')

@client.command()
async def clear(ctx, amount= 100):
  await ctx.channel.purge(limit=amount,check=lambda msg: not msg.pinned)


my_secret = os.environ['TOKEN']
client.run(os.getenv('TOKEN'))
import discord
import os
from discord.ext import commands
question = input
TOKEN = 'ODIyMTk1NDM4NTM4OTgxMzk3.YFOvLA.4TaeBKNNZOgg-Xho1nhoEWkG_GY'


client = commands.Bot(command_prefix = 'j!')

@client.command()
async def ping(ctx):
  await ctx.send('Pong!')

@client.event
async def on_ready():
  await client.change_presence(status=discord.Status.idle, activity=discord.Game('with her heart'))
  print('Bot is ready!')


client.run(TOKEN)
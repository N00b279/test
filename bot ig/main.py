import os, discord, random, string, asyncio, aiohttp
from discord.ext import commands
from discord.ui import Button, Select, View
from googletrans import Translator

bot = commands.Bot(command_prefix=">", intents=discord.Intents.all())

@bot.event
async def on_ready():
    print("Ready!")

@bot.command()
async def ping(ctx):
    await ctx.send(f"Pong! `{round(bot.latency * 1000)}ms`")

counter = 0
for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')
        print(f'Loaded cog: {filename[:-3]}')
        counter += 1
print(f'Finished loading [{counter}] cogs')

bot.run("OTgxMTA0MjQyNDEwNTM2OTcw.GKsjGY.NjwQMGdTpe7OjpAJXK2S16gPYuaU_nrbqf1c0A")
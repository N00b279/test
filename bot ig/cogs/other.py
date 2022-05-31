import os, discord, random, string, asyncio, aiohttp
from discord.ext import commands


class other(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def echo(self, ctx, *, message):
        await ctx.send(message)
        await ctx.message.delete()

    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f"Pong! `{round(self.bot.latency * 1000)}ms`")
        
def setup(bot):
    bot.add_cog(other(bot))
import os, discord, random, string, asyncio, aiohttp
from discord.ext import commands


class utils(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    @commands.has_permissions(manage_channels=True)
    async def slowmode(self, ctx, time:int):
        if seconds < 0:
            embed = discord.Embed(title="",description=f"Slowmode must be more then `0`!",color=0x2ecc71)
            await ctx.send(embed=embed)
            return
        if seconds > 21600:
            embed = discord.Embed(title="",description=f"Slowmode must be less then `21600`! `{seconds}/21600`",color=0x2ecc71)
            await ctx.send(embed=embed)
            return
        if seconds == 1:
            embed = discord.Embed(title="",description=f"Slowmode set to **{seconds}** second",color=0x2ecc71)
            await ctx.send(embed=embed)
            await ctx.channel.edit(slowmode_delay=seconds)
        else:
            embed = discord.Embed(title="",description=f"Slowmode set to **{seconds}** seconds",color=0x2ecc71)
            await ctx.send(embed=embed)
            await ctx.channel.edit(slowmode_delay=seconds)
        
    @commands.command(aliases=['clear'])
    @commands.has_permissions(manage_messages=True)
    async def purge(self, ctx, amount: int):
        if amount > 1000:
            await ctx.send(f"Must be less than `1000`. `{amount}/1000`")
        if amount < 0:
            await ctx.send(f"Must be more than `0`.")
        else:
            await ctx.channel.purge(limit=amount + 1)
            embed = discord.Embed(title="",description=f"Purged `{amount}` messages!",color=0x2ecc71)
            await ctx.send(embed=embed, delete_after=5)
            
def setup(bot):
    bot.add_cog(utils(bot))
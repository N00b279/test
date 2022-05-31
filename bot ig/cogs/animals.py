import os, discord, random, string, asyncio, aiohttp
from discord.ext import commands


class animals(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def cat(self,ctx):
        async with aiohttp.ClientSession() as cs:
            async with cs.get('https://some-random-api.ml/animal/cat') as r:
                res = await r.json()
        em = discord.Embed(title="Random Cat 🐈", color=0xFFCD4D)
        em.set_image(url=res['image'])
        em.set_footer(text="Requested From: some-random-api.ml/animal/cat")
        await ctx.send(embed=em)

    @commands.command()
    async def dog(self,ctx):
        async with aiohttp.ClientSession() as cs:
            async with cs.get('https://some-random-api.ml/animal/dog') as r:
                res = await r.json()
        em = discord.Embed(title="Random Dog 🐕", color=0xDA9F83)
        em.set_image(url=res['image'])
        em.set_footer(text="Requested From: some-random-api.ml/animal/dog")
        await ctx.send(embed=em)

    @commands.command()
    async def birb(self,ctx):
        async with aiohttp.ClientSession() as cs:
            async with cs.get('https://some-random-api.ml/animal/birb') as r:
                res = await r.json()
        em = discord.Embed(title="Random Birb 🐦", color=0xDD2E44)
        em.set_image(url=res['image'])
        em.set_footer(text="Requested From: some-random-api.ml/animal/birb")
        await ctx.send(embed=em)
        
def setup(bot):
    bot.add_cog(animals(bot))
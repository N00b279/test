import os, discord, random, string, asyncio, aiohttp
from discord.ext import commands


class user(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.user_command(name = "Get Avatar")
    async def uavatar(self, ctx, user):
        embed = discord.Embed(title=f"{user}'s Avatar",color=0xffcc4d)
        embed.set_image(url=user.avatar)
        await ctx.respond(embed=embed)    
        
def setup(bot):
    bot.add_cog(user(bot))
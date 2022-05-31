import os, discord, random, string, asyncio, aiohttp
from discord.ext import commands


class mod(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, *, reason=None):
        if member == ctx.author:
            await ctx.send("You cant ban yourself!")
        else:
            await member.ban(reason=reason)
            embed = discord.Embed(title=f"",description=f"**Banned** {member.mention}",color=0xe74c3c)
            await ctx.send(embed=embed)

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        if member == ctx.author:
            await ctx.send("You cant kick yourself!")
        else:
            await member.kick(reason=reason)
            embed = discord.Embed(title=f"",description=f"**Kicked** {member.mention}",color=0xe74c3c)
            await ctx.send(embed=embed)

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def mute(self, ctx, member: discord.Member, *, reason=None):
        guild = ctx.guild
        mutedRole = discord.utils.get(ctx.guild.roles, name="Time Out")

        if not mutedRole:
            mutedRole = await guild.create_role(name="Time Out")

            for channel in guild.channels:
                await channel.set_permissions(mutedRole,speak=False,send_messages=False,read_message_history=True,read_messages=False)

        await member.add_roles(mutedRole, reason=reason)
        embed = discord.Embed(title=f"",description=f"**Muted** {member.mention}",color=0xe74c3c)
        await ctx.send(embed=embed)
    
def setup(bot):
    bot.add_cog(mod(bot))
from discord.ext import commands
from discord.ext.commands.errors import CheckFailure
import discord

class Mod(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name = 'Kick')
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member : discord.Member, *, reason = None):
        await member.kick(reason=reason)

    @kick.error()
    async def ke(self, ctx, error):
        if isinstance(error, missing_perms):
            await ctx.send('Noob you do not have the perms')

def setup(bot):
    bot.add_cog(Mod(bot))
##> Imports
# > Discord dependencies
import discord
from discord.ext import commands


class Listeners(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener(name="on_command")
    async def print(self, ctx):
        print(f"{ctx.author} used !{ctx.command} in channel {ctx.message.channel}")

    # On member join
    @commands.Cog.listener()
    async def on_member_join(self, member):
        """ Gives new users the role Tryout """
        role = discord.utils.get(member.guild.roles, name="Tryout")
        await member.add_roles(role)


def setup(bot):
    bot.add_cog(Listeners(bot))

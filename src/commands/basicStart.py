# I recommend using class
import discord
from discord.ext import commands

# you can inherit from commands.cog
# I strongly recommend reading the documentation to understand
class CommandsBasic(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    """YOUR COMMAND"""
    @commands.command(name="name of your command")
    async def command(self, ctx:commands.Context):
        await ctx.send("My primary command")


# simple? yes?, ok
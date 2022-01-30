import discord
from discord.ext import commands
from discord.ext.commands import has_permissions
from functions import botbancheck

class Tags(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    

def setup(bot):
    bot.add_cog(Tags(bot))
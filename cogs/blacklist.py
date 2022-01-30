import discord, json, os, asyncio, datetime
from discord.ext import commands
from discord_components import DiscordComponents
from functions import botbancheck
from dotenv import load_dotenv

load_dotenv()
prefix = os.getenv('PREFIX')

def lf():
    with open('json/Botban.json') as f:
        data = json.load(f)
    return data

def wf(data):
    with open('json/Botban.json', 'w') as f:
        json.dump(data, f, indent=4)

class Blacklist(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    @commands.is_owner()
    async def botban(self, ctx, user:discord.User):
        data = lf()
        if user.id in data['botbannedusers']:
            await ctx.send("User is already blacklisted")
        else:
            data['botbannedusers'].append(user.id)
            wf(data)
            await ctx.send(embed=discord.Embed(title="Successful blacklist", description=f"{user.mention} has been blacklisted", color=discord.Color.random()))
    
    @commands.command()
    @commands.is_owner()
    async def botunban(self, ctx, user:discord.User):
        data = lf()
        if user.id not in data['botbannedusers']:
            await ctx.send("User is not blacklisted")
        else:
            data['botbannedusers'].pop(data['botbannedusers'].index(user.id))
            wf(data)
            await ctx.send(embed=discord.Embed(title="Successful blacklist", description=f"<@{id}> has been unblacklisted", color=discord.Color.random()))

    @commands.command(aliases=['bl'])
    @commands.is_owner()
    async def blacklist(self, ctx):
        data = lf()
        embed=discord.Embed(title="Blacklisted Users", color=discord.Color.random())
        u = ""
        for id in data['botbannedusers']:
          u = u + f"<@!{id}>"
        embed.description = u
        await ctx.reply(embed=embed, mention_author=False)

def setup(bot):
    bot.add_cog(Blacklist(bot))
import discord, json, os, asyncio, datetime
from discord.ext import commands
from discord_components import DiscordComponents
from functions import botbancheck
from dotenv import load_dotenv

load_dotenv()
prefix = os.getenv('PREFIX')

def lf():
    with open('json/info.json') as f:
        data = json.load(f)
    return data

def wf(data):
    with open('json/info.json', 'w') as f:
        json.dump(data, f, indent=4)

class Other(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        DiscordComponents(self.bot)
        print(f"Logged in as {self.bot.user} ({self.bot.user.id})")
        await self.bot.change_presence(status=discord.Status.idle, activity=discord.Game(f"{prefix}help"))
		await self.bot.fetch_channel(935144122019373086).send("I am online")
		
        data = lf()
        try:
            del data['START_TIME']
        except:
            pass
        data['START_TIME'] = round(datetime.datetime.now().timestamp())
        wf(data)

    @commands.command(aliases=['latency'])
    @botbancheck()
    async def ping(self, ctx):
        await ctx.send(f"Latency:- `{round(self.bot.latency*1000)} ms`")

    @commands.command(aliases=['stat', 'status'])
    @botbancheck()
    async def stats(self, ctx):
        embed=discord.Embed(color=discord.Color.random())
        embed.add_field(name="Uptime since", value=f"<t:{lf()['START_TIME']}:R>")
        embed.add_field(name="Latency", value=f"{round(self.bot.latency*1000)} ms")
        embed.add_field(name="Guild count", value=len(self.bot.guilds))
        m = 0
        for g in self.bot.guilds:
            m += g.member_count
        embed.add_field(name="Member count", value=m)
        embed.add_field(name="Shards", value="Not sharded")
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Other(bot))
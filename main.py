import discord, os
from discord.ext import commands
from dotenv import load_dotenv
from webserver import keep_alive

load_dotenv()
prefix = os.getenv('PREFIX')
intents = discord.Intents.all()
bot = commands.Bot(command_prefix=prefix, intents=intents)

@bot.command()
@commands.is_owner()
async def load(ctx, extension):
    try:
        bot.load_extension(f"cogs.{extension}")
        await ctx.send(f"Loaded extension:- `{extension}`")
    except Exception as error:
        await ctx.send(error)
        await ctx.send(type(error))
@load.error
async def error(ctx, e):
    await ctx.send(e)

@bot.command()
@commands.is_owner()
async def unload(ctx, extension):
    try:
        bot.unload_extension(f"cogs.{extension}")
        await ctx.send(f"Unloaded extension:- `{extension}`")
    except Exception as error:
        await ctx.send(error)
        await ctx.send(type(error))
@unload.error
async def error(ctx, e):
    await ctx.send(e)

@bot.command()
@commands.is_owner()
async def reload(ctx, extension):
    try:
        bot.unload_extension(f"cogs.{extension}")
        bot.load_extension(f"cogs.{extension}")
    except:
        bot.load_extension(f"cogs.{extension}")
    await ctx.send(f"Reloaded extension:- `{extension}`")
@reload.error
async def error(ctx, e):
    await ctx.send(e)

@bot.command()
@commands.is_owner()
async def refresh(ctx):
    for file in os.listdir('cogs'):
        if file.endswith('.py'):
            try:
                bot.unload_extension(f'cogs.{file[:-3]}')
                bot.load_extension(f'cogs.{file[:-3]}')
            except:
                bot.load_extension(f'cogs.{file[:-3]}')
    await ctx.send(f"Refreshed extensions")
@refresh.error
async def error(ctx, e):
    await ctx.send(e)

for file in os.listdir('cogs'):
    if file.endswith('.py'):
        bot.load_extension(f'cogs.{file[:-3]}')
        print(f"Loaded extension:- {file}")

# custom_load = []
# for cl in custom_load:
#     bot.load_extension(f'cogs.{cl}')
#     print(f"Loaded extension:- {cl}")

bot.load_extension('jishaku')
print(f"Loaded extension:- jishaku")

# keep_alive()
bot.run(os.getenv('TOKEN'))
import os, json, discord
from discord.ext import commands
from dotenv import load_dotenv
load_dotenv()

def lf():
    with open('json/Botban.json') as f:
        data = json.load(f)
    return data

def botbancheck():
    def predicate(ctx):
        return ctx.message.author.id not in lf()['botbannedusers']
    return commands.check(predicate)
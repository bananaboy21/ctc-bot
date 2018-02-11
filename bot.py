import discord
import os
import io
import traceback
import sys
import time
import datetime
import asyncio
import random
import aiohttp
import pip
import random
import textwrap
from contextlib import redirect_stdout
from discord.ext import commands
import json
bot = commands.Bot(command_prefix=commands.when_mentioned_or('$'),description="Specialized bot made for COC Talk Club.\n\nHelp Commands",owner_id=277981712989028353)
bot.remove_command("help")

@bot.event
async def on_ready():
    print('Bot is online, and ready to ROLL!')
    await bot.change_presence(game=discord.Game(name="$help"))


@bot.command()
async def help(ctx):
    color = discord.Color(value=0x00ff00)
    em = discord.Embed(color=color, title='COC Talk Club Bot')
    em.add_field(name="twitter", value="Returns the CTC's Twitter page.")
    em.add_field(name="website", value="Returns the CTC's official website.")
    em.add_field(name="logo", value="Returns facts for the COC Talk Club logo!")
    em.add_field(name="leagues", value="Returns invite links to some COC leagues!")
    em.add_field(name="tourney", value="Returns invite links to some COC tournaments!")
    em.add_field(name="communities", value="Returns invite links to some COC communities!")
    em.add_field(name="bots", value="Returns invite links to some Discord bot servers!")
    em.add_field(name="gfx", value="Returns Discord usernames of some amazing COC GFX designers!")
    em.set_thumbnail(url="https://media.discordapp.net/attachments/410033646309736448/410205224213413889/JPEG_20180126_122140.jpg")
    await ctx.send(embed=em)



@bot.command()
async def twitter(ctx):
    await ctx.send("Check out Coc Talk Club (@CTC_coc): https://twitter.com/CTC_coc?s=09")


@bot.command()
async def website(ctx):
    await ctx.send("https://coctalkclub.weebly.com/")


@bot.command()
async def logo(ctx):
    await ctx.send("The first logo was made by Abuxine Gaming and Jitux Made 3 logos for CTC and Nick clashes made 1 one logo for CTC")


@bot.command()
async def leagues(ctx):
    color = discord.Color(value=0x00ff00)
    em = discord.Embed(color=color, title='COC Leagues')
    em.description = 'Here are some leagues to join! \n\nWCL: https://discord.gg/Hwk9SbW \nBWC: https://discord.gg/W5EgkRH \nICWL: https://discord.gg/fNTRU32 \nNCWL: discord.me/ncwl \nGauntlet: https://discord.gg/2XtH5nE \nAWL: https://discord.gg/WbK39GJ'
    await ctx.send(embed=em)


@bot.command()
async def tourney(ctx):
	color = discord.Color(value=0x00ff00)
    em = discord.Embed(color=color, title='COC Tournaments')
    em.description = 'Here are some COC tourneys to join! \n\nClash Champs: https://discord.gg/a95eHnq \nCPE: https://discord.gg/XAEx6Hf \nForums Cup: https://discord.gg/8RNXdXR'
    await ctx.send(embed=em)


@bot.command()
async def communities(ctx):
	color = discord.Color(value=0x00ff00)
    em = discord.Embed(color=color, title='COC Communities')
    em.description = "Here are some COC communities to join! \n\nIndian Clash Community: https://discord.gg/qg8wPtv \nCasual Clash: https://discord.io/clash \nClash Tutor: https://discord.gg/SYDB7K9\nSouth African Clash Community: https://discord.gg/HVt929x\nBase Building: https://discord.gg/HR8zT4M\nClash Roulette: https://discord.me/roulette\nPotluck: https://discord.me/cocpotluck\nForums vs Reddit: https://discord.gg/JE86z7c\nCoc Bromance: https://discord.gg/KWjve7c\nGoblins Realm: https://discord.gg/qgSrda2\nZillas Fam: https://discord.gg/bJbj65x\nClash Connections: https://discord.gg/CN9VW3B\nClash Art community: https://discord.gg/BWcbUH7"
    await ctx.send(embed=em)


@bot.command()
async def bots(ctx):
	color = discord.Color(value=0x00ff00)
    em = discord.Embed(color=color, title='Discord Bots')
    em.description = "Here are the servers for some Discord bots. \n\ndat banana bot: https://discord.gg/wvkVknA\nMyBot: https://discord.gg/4ZeNS74\nWmbot: https://discord.me/warmatch\nSidekick-https://discord.gg/ENYgjk"
    await ctx.send(embed=em)


@bot.command()
async def gfx(ctx):
	color = discord.Color(value=0x00ff00)
    em = discord.Embed(color=color, title='Clash of Clans GFX Designers')
    em.description = "Jitux3xD#6545 \nNick clashes#8401  \nBangBangAure#3966 \nBobby_digital72#5621 \nMiss.Behavin#6462 \nfiRe loRd#2593  \nBox, Clash & Art!#8519 \nMini Me#2525"
    await ctx.send(embed=em)



if not os.environ.get('TOKEN'):
    print("no token found REEEE!")
bot.run(os.environ.get('TOKEN').strip('"'))

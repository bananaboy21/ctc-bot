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
	em.add_field(name="logo", value="Returns facts for the CTC's logo!")
	em.add_field(name="leagues", value="Returns invite links to some COC leagues!")
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
	em.description = 'Here are some leagues to join!'
	em.add_field(name="WCL", value="https://discord.gg/kD7VW78")
	em.add_field(name="ICWL", value="https://discord.gg/fNTRU32")
	em.add_field(name="NCWL", value="https://discord.gg/fNTRU32")
	em.add_field(name="Gauntlet", value="https://discord.gg/2XtH5nE")
	em.add_field(name="AWL", value="https://discord.gg/WbK39GJ")
	em.add_field(name="Clash Champs", value="https://discord.gg/a95eHnq")
	await ctx.send(embed=em)


if not os.environ.get('TOKEN'):
    print("no token found REEEE!")
bot.run(os.environ.get('TOKEN').strip('"'))

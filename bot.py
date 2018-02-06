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


@bot.event
async def on_ready():
    print('Bot is online, and ready to ROLL!')
	await bot.change_presence(game=discord.Game(name="$help"))


@bot.command()
async def twitter(ctx):
	await ctx.send("Check out Coc Talk Club (@CTC_coc): https://twitter.com/CTC_coc?s=09")


@bot.command()
async def website(ctx):
	await ctx.send("https://coctalkclub.weebly.com/")


@bot.command()
async def logo(ctx):
	await ctx.send("The first logo was made by Abuxine Gaming and Jitux Made 3 logos for CTC and Nick clashes made 1 one logo for CTC")


if not os.environ.get('TOKEN'):
    print("no token found REEEE!")
bot.run(os.environ.get('TOKEN').strip('"'))
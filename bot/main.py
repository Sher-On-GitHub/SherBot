from nextcord import *
from nextcord.abc import GuildChannel
import nextcord
import random, os, json, datetime, time, asyncio, aiosqlite
from nextcord.ext import commands, tasks
from nextcord.ui import Button, View, Select
from os import environ
from dotenv import load_dotenv
load_dotenv()
token = environ["BOT_TOKEN"]

intents = nextcord.Intents.default()
intents.message_content = True
intents.messages = True
intents.guilds = True
intents.members = True
bot = commands.Bot(command_prefix="/", intents=intents)
helpGuide = json.load(open('bot/help.json'))

def createHelpEmbed(pageNum=0, inline=False):
	pageNum = (pageNum) % len(list(helpGuide))
	pageTitle = list(helpGuide)[pageNum]
	embed=Embed(color=nextcord.Color.green(), title=pageTitle)
	for key, val in helpGuide[pageTitle].items():
		embed.add_field(name="/"+key, value=val, inline=inline)
		embed.set_footer(text=f"Page {pageNum+1} of {len(list(helpGuide))}")
	return embed
    
@bot.slash_command(name="help", description="Displays command help menu.")
async def help(ctx:Interaction):
    currentPage = 0
    async def next_callback(interaction):
        nonlocal currentPage, sent_msg
        currentPage += 1
        await sent_msg.edit(embed=createHelpEmbed(pageNum=currentPage), view=myview)
    async def previous_callback(interaction):
        nonlocal currentPage, sent_msg
        currentPage -= 1
        await sent_msg.edit(embed=createHelpEmbed(pageNum=currentPage), view=myview)
    nextButton = Button(label=">", style=ButtonStyle.green)
    nextButton.callback = next_callback
    previousButton = Button(label="<", style=ButtonStyle.green)
    previousButton.callback =  previous_callback
    myview = View(timeout=180)
    myview.add_item(previousButton)
    myview.add_item(nextButton)
    sent_msg = await ctx.send(embed=createHelpEmbed(pageNum=currentPage), view=myview)
    print("Executed command.")

for fn in os.listdir("bot/commands"):
    if fn.endswith(".py"):
        bot.load_extension(f"commands.{fn[:-3]}")
for fn in os.listdir("bot/events"):
    if fn.endswith(".py"):
        bot.load_extension(f"events.{fn[:-3]}")
for fn in os.listdir("bot/levelsystem"):
    if fn.endswith(".py"):
        bot.load_extension(f"levelsystem.{fn[:-3]}")

bot.run(token)
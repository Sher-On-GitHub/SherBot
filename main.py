from nextcord import *
import nextcord, os
from nextcord.ext import commands
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

for fn in os.listdir("./commands"):
    if fn.endswith(".py"):
        bot.load_extension(f"commands.{fn[:-3]}")
for fn in os.listdir("./events"):
    if fn.endswith(".py"):
        bot.load_extension(f"events.{fn[:-3]}")
for fn in os.listdir("./levelsystem"):
    if fn.endswith(".py"):
        bot.load_extension(f"levelsystem.{fn[:-3]}")

from nextcord import Interaction, SlashOption, ChannelType, Member, Embed, File, ButtonStyle, colour, errors, ApplicationInvokeError, SelectOption, application_command, ApplicationCommandOption
import nextcord, random, os, json, datetime, time, aiosqlite
from nextcord.ext import commands, tasks
from itertools import cycle
from nextcord.ui import Button, View, Select
global startTime
startTime = time.time()

intents = nextcord.Intents.default()
intents.message_content = True
intents.messages = True
intents.guilds = True
intents.members = True
bot = commands.Bot(command_prefix="/", intents=intents)

class Events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_connect(self):
        print("Online.")

def setup(bot):
    bot.add_cog(Events(bot))
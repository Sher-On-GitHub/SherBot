from nextcord import *
from nextcord.abc import GuildChannel
import nextcord
import random, os, json, datetime, time, asyncio, aiosqlite, requests
from nextcord.ext import commands, tasks
from nextcord.ui import Button, View, Select
global startTime
startTime = time.time()

intents = nextcord.Intents.default()
intents.message_content = True
intents.messages = True
intents.guilds = True
intents.members = True
bot = commands.Bot(command_prefix="/", intents=intents)

class Image(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @nextcord.slash_command(name="cat", description="Displays an image containing one or more cats.")
    async def cat(self, interaction:Interaction):
        await interaction.response.defer()
        data = requests.get("https://api.thecatapi.com/v1/images/search")
        data = data.json()
        get = data[0]
        result = get["url"]
        embed = nextcord.Embed(
            title="Cat!",
            color=nextcord.Color.green()
        )
        embed.set_image(url=result)
        embed.timestamp = datetime.datetime.now()
        embed.set_footer(text = "SherBot", icon_url = "https://cdn.discordapp.com/attachments/1031828036422733825/1044698179179909290/abitgreener.png")
        await interaction.edit_original_message(embed=embed)
        print("Command executed successfully.")

    @nextcord.slash_command(name="dog", description="Displays an image containing one or more dogs.")
    async def dog(self, interaction: Interaction):
        await interaction.response.defer()
        data = requests.get("https://api.thedogapi.com/v1/images/search")
        data = data.json()
        get = data[0]
        result = get["url"]
        embed = nextcord.Embed(
            title="Dog!",
            color=nextcord.Color.green()
        )
        embed.set_image(url=result)
        embed.timestamp = datetime.datetime.now()
        embed.set_footer(text = "SherBot", icon_url = "https://cdn.discordapp.com/attachments/1031828036422733825/1044698179179909290/abitgreener.png")
        await interaction.edit_original_message(embed=embed)
        print("Command executed successfully.")

def setup(bot):
    bot.add_cog(Image(bot))
from nextcord import *
from nextcord.abc import GuildChannel
import nextcord
import random, os, json, datetime, time, asyncio, aiosqlite
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

class Informative(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @nextcord.slash_command(name="botinfo", description="Provides information about SherBot.")
    async def botinfo(self, ctx:Interaction):
        embed = nextcord.Embed(title="SherBot Info", color=nextcord.Color.green())
        embed.add_field(name="Language: ", value="Python 3.11.0", inline=True)
        embed.add_field(name="Library: ", value="Nextcord 2.3.2", inline=True)
        embed.add_field(name="Uptime: ", value=str(datetime.timedelta(seconds=int(round(time.time()-startTime)))), inline=True)
        embed.add_field(name="Latency: ", value=(f"{round(self.bot.latency * 1000)}ms"), inline=True)
        await ctx.send(embed=embed)
        print("Command executed successfully.")

    @nextcord.slash_command(name="userinfo", description="Provides information about a user.")
    async def userinfo(self, ctx:Interaction, member : nextcord.Member):
        embed = nextcord.Embed(title=f"{member} - User Information", color=nextcord.Color.green())
        embed.add_field(name="ID: ", value=member.id, inline=False)
        embed.add_field(name="Account created: ", value=member.created_at.strftime("%a, %#d %B %Y, %I:%M %p EST"), inline=False)
        embed.add_field(name="Joined at: ", value=member.joined_at.strftime("%a, %#d %B %Y, %I:%M %p EST"), inline=False)
        embed.add_field(name="Bot? ", value=member.bot, inline=False)
        embed.timestamp = datetime.datetime.now()
        embed.set_footer(text="SherBot", icon_url="https://cdn.discordapp.com/attachments/1031828036422733825/1044698179179909290/abitgreener.png")
        await ctx.send(embed=embed)
        print("Command executed successfully.")

    @nextcord.slash_command(name="serverinfo", description="Provides information about the guild.")
    async def serverinfo(self, ctx:Interaction):
        embed = nextcord.Embed(title = f"{ctx.guild.name} Info", color = nextcord.Colour.green())
        embed.add_field(name = 'Server ID', value = f"{ctx.guild.id}", inline = False)
        embed.add_field(name = 'Created On', value = ctx.guild.created_at.strftime("%a, %#d %B %Y, %I:%M %p EST"), inline = False)
        embed.add_field(name = 'Members', value = f'{ctx.guild.member_count} Members', inline = False)
        embed.add_field(name = 'Channels', value=f'{len(ctx.guild.text_channels)} Text Channel(s) | {len(ctx.guild.voice_channels)} Voice Channel(s)', inline=True)
        embed.set_thumbnail(url = ctx.guild.icon)
        embed.timestamp = datetime.datetime.now()
        embed.set_footer(text = "SherBot", icon_url = "https://cdn.discordapp.com/attachments/1031828036422733825/1044698179179909290/abitgreener.png")
        await ctx.send(embed=embed)
        print("command executed successfully.")

def setup(bot):
    bot.add_cog(Informative(bot))
from nextcord import *
from nextcord.abc import GuildChannel
import nextcord
import random, os, json, datetime, time, asyncio, aiosqlite, humanfriendly
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

class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @nextcord.slash_command(name="kick", description="Kicks a user.")
    @commands.has_guild_permissions(kick_members=True)
    async def kick(self, ctx: Interaction, member: nextcord.Member, reason="No reason given"):
        await member.kick(reason=reason)
        embed=nextcord.Embed(color=nextcord.Color.green())
        embed.add_field(name="User Kicked.", value=f"Reason: {reason}", inline=False)
        embed.timestamp = datetime.datetime.now()
        embed.set_footer(text = "SherBot", icon_url = "https://cdn.discordapp.com/attachments/1031828036422733825/1044698179179909290/abitgreener.png")
        await ctx.send(embed=embed)
        print("Command executed successfully.")

    @kick.error
    async def kickerror(ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Please fill in all required arguments!")
        elif isinstance(error, commands.MissingPermissions):
            await ctx.send("You do not have the required permissions to execute this command!")
        elif isinstance(error, commands.MemberNotFound):
            await ctx.send("Member not found!")

    @nextcord.slash_command(name="ban", description="Bans a user.")
    @commands.has_guild_permissions(ban_members=True)
    async def ban(self, ctx: Interaction, member: nextcord.Member, reason="No reason given"):
        await member.ban(reason=reason)
        embed=nextcord.Embed(color=nextcord.Color.green())
        embed.add_field(name="User banned.", value=f"Reason: {reason}")
        embed.timestamp = datetime.datetime.now()
        embed.set_footer(text = "SherBot", icon_url = "https://cdn.discordapp.com/attachments/1031828036422733825/1044698179179909290/abitgreener.png")
        await ctx.send(embed=embed)
        print("Command executed successfully.")

    @ban.error
    async def banerror(ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Please fill in all required arguments!")
        elif isinstance(error, commands.MissingPermissions):
            await ctx.send("You do not have the required permissions to execute this command!")
        elif isinstance(error, commands.MemberNotFound):
            await ctx.send("Member not found!")

    @nextcord.slash_command(name="clear", description="Deletes a specified amount of messages.")
    @commands.has_guild_permissions(manage_messages=True)
    async def clear(self, ctx: Interaction, amount: int):
        if amount != int:
            await ctx.send("Insert an integer!")
        else:
            await ctx.channel.purge(limit=amount + 1)
            embed=nextcord.Embed(color=nextcord.Color.green())
            embed.add_field(name="Cleared!", value=f"Messages cleared: {amount}")
            embed.timestamp = datetime.datetime.now()
            embed.set_footer(text = "SherBot", icon_url = "https://cdn.discordapp.com/attachments/1031828036422733825/1044698179179909290/abitgreener.png")
            await ctx.send(embed=embed)
            print("Command executed successfully.")

    @clear.error
    async def clearerror(ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Please fill in all required arguments!")
        elif isinstance(error, commands.MissingPermissions):
            await ctx.send("You do not have the required permissions to execute this command!")

    @nextcord.slash_command(name="mute", description="Mutes a user for a specified amount of time.")
    @commands.has_guild_permissions(moderate_members=True)
    async def mute(self, ctx:Interaction, member : nextcord.Member, time, reason="No reason given"):
        time = humanfriendly.parse_timespan(time)
        await member.edit(timeout=nextcord.utils.utcnow()+datetime.timedelta(seconds=time))
        embed=nextcord.Embed(color=nextcord.Color.green())
        embed.add_field(name=f"{member} has been muted.", value=f"Reason: {reason}")
        embed.timestamp = datetime.datetime.now()
        embed.set_footer(text = "SherBot", icon_url = "https://cdn.discordapp.com/attachments/1031828036422733825/1044698179179909290/abitgreener.png")
        await ctx.send(embed=embed)
        print("Command executed successfully.")

    @mute.error
    async def muteerror(ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Please fill in all required arguments!")
        elif isinstance(error, commands.MissingPermissions):
            await ctx.send("You do not have the required permissions to execute this command!")
        elif isinstance(error, commands.MemberNotFound):
            await ctx.send("Member not found!")

    @nextcord.slash_command(name="unmute", description="Unmutes a user.")
    @commands.has_guild_permissions(moderate_members=True)
    async def unmute(self, ctx:Interaction, member:nextcord.Member):
        if member.timeout == True:
            await member.edit(timeout=None)
            await ctx.send(f"{member.mention} has been unmuted!")
            print("Command executed successfully.")
        else:
            ctx.send("This user is not muted.")

    @unmute.error
    async def unmuteerror(ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Please fill in all required arguments!")
        elif isinstance(error, commands.MissingPermissions):
            await ctx.send("You do not have the required permissions to execute this command!")
        elif isinstance(error, commands.MemberNotFound):
            await ctx.send("Member not found!")

def setup(bot):
    bot.add_cog(Moderation(bot))
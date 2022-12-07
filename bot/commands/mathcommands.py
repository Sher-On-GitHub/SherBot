from nextcord import *
import nextcord
import datetime, time
from nextcord.ext import commands, tasks
global startTime
startTime = time.time()

intents = nextcord.Intents.default()
intents.message_content = True
intents.messages = True
intents.guilds = True
intents.members = True
bot = commands.Bot(command_prefix="/", intents=intents)

class Math(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @nextcord.slash_command(name="add", description="Adds two numbers together.")
    async def add(self, ctx:Interaction, num1, num2):
            result = int(num1) + int(num2)
            embed = nextcord.Embed(title=f"Equation: {num1} + {num2}", description=f"Result: {result}", color=nextcord.Color.green())
            await ctx.send(embed=embed)
            print("Command executed successfully.")

    @nextcord.slash_command(name="subtract", description="Subtracts on number from another.")
    async def subtract(self, ctx, num1, num2):
            result = int(num1) - int(num2)
            embed = nextcord.Embed(title=f"Equation: {num1} - {num2}", description=f"Result: {result}", color=nextcord.Color.green())
            await ctx.send(embed=embed)
            print("Command executed successfully.")

    @nextcord.slash_command(name="multiply", description="Multiplies two numbers.")
    async def multiply(self, ctx:Interaction, num1, num2):
            result = int(num1) * int(num2)
            embed = nextcord.Embed(title=f"Equation: {num1} x {num2}", description=f"Result: {result}", color=nextcord.Color.green())
            await ctx.send(embed=embed)
            print("Command executed successfully.")

    @nextcord.slash_command(name="divide", description="Divides two numbers.")
    async def divide(self, ctx, num1, num2):
            result = int(num1) / int(num2)
            embed = nextcord.Embed(title=f"Equation: {num1} ÷ {num2}", description=f"Result: {result}", color=nextcord.Color.green())
            await ctx.send(embed=embed)
            print("Command executed successfully.")

def setup(bot):
    bot.add_cog(Math(bot))

from nextcord import *
import nextcord, json
import time
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

helpGuide = json.load(open("bot/commands/help.json"))

def createHelpEmbed(pageNum=0, inline=False):
	pageNum = (pageNum) % len(list(helpGuide))
	pageTitle = list(helpGuide)[pageNum]
	embed=Embed(color=nextcord.Color.green(), title=pageTitle)
	for key, val in helpGuide[pageTitle].items():
		embed.add_field(name="/"+key, value=val, inline=inline)
		embed.set_footer(text=f"Page {pageNum+1} of {len(list(helpGuide))}")
	return embed

class HelpCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @nextcord.slash_command(name="help", description="Displays command help menu.")
    async def help(self, ctx:Interaction):
        currentPage = 0
        async def next_callback(interaction):
            nonlocal currentPage, sent_msg
            currentPage += 1
            await sent_msg.edit(embed=createHelpEmbed(pageNum=currentPage), view=myview)
        async def previous_callback(interaction):
            nonlocal currentPage, sent_msg
            currentPage -= 1
            await sent_msg.edit(embed=createHelpEmbed(pageNum=currentPage), view=myview)
        nextButton = Button(label="→", style=ButtonStyle.green)
        nextButton.callback = next_callback
        previousButton = Button(label="←", style=ButtonStyle.green)
        previousButton.callback =  previous_callback
        myview = View(timeout=180)
        myview.add_item(previousButton)
        myview.add_item(nextButton)
        sent_msg = await ctx.send(embed=createHelpEmbed(pageNum=currentPage), view=myview)
        print("Executed command.")

def setup(bot):
    bot.add_cog(HelpCommand(bot))

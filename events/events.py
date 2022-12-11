import nextcord, time
from nextcord.ext import commands
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
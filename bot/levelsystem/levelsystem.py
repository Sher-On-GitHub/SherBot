from nextcord import *
import nextcord, random, os, json, datetime, time, aiosqlite
from nextcord.ext import commands, tasks
from itertools import cycle
from nextcord.ui import Button, View, Select

intents = nextcord.Intents.default()
intents.message_content = True
intents.messages = True
intents.guilds = True
intents.members = True
bot = commands.Bot(command_prefix="/", intents=intents)

class LevelSystem(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Level system online.")
        global startTime
        startTime = time.time()
        setattr(bot, "db", await aiosqlite.connect("level.db"))
        async with aiosqlite.connect("level.db") as db:
            async with db.cursor() as cursor:
                await cursor.execute('CREATE TABLE IF NOT EXISTS levels (level INTEGER , xp INTEGER, user INTEGER, guild INTEGER)')
            await db.commit()

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return
        author = message.author
        guild = message.guild
        async with bot.db.cursor() as cursor:
            await cursor.execute('SELECT xp FROM levels WHERE user = ? AND guild = ?', (author.id, guild.id,))
            xp = await cursor.fetchone()
            await cursor.execute('SELECT level FROM levels WHERE user = ? AND guild = ?', (author.id, guild.id,))
            level = await cursor.fetchone()

            if not xp or not level:
                await cursor.execute('INSERT INTO levels (level, xp, user, guild) VALUES (?, ?, ?, ?)', (0, 0, author.id, guild.id,))
            await bot.db.commit()
            
            try:
                xp = xp[0]
                level = level[0]
            except TypeError:
                xp = 0
                level = 0

            if level < 5:
                xp += random.randint(5, 7)
                await cursor.execute('UPDATE levels SET xp = ? WHERE user = ? AND guild = ?', (xp, author.id, guild.id,))
            else:
                rand = random.randint(1, (level//4))
                if rand == 1:
                    xp += random.randint(1, 3)
                    await cursor.execute('UPDATE levels SET xp = ? WHERE user = ? AND guild = ?', (xp, author.id, guild.id,))
            if xp >= 120:
                level += 1
                await cursor.execute('UPDATE levels SET level = ? WHERE user = ? AND guild = ?', (level, author.id, guild.id,))
                await cursor.execute('UPDATE levels SET xp = ? WHERE user = ? AND guild = ?', (0, author.id, guild.id,))
                await message.channel.send(f'{author.mention} has leveled up to level **{level}**!')
            await bot.db.commit()

    @nextcord.slash_command(name="level", description="Displays a users level in the SherBot Level System.")
    async def level(self, ctx:Interaction, member : nextcord.Member):
        async with bot.db.cursor() as cursor:
            await cursor.execute('SELECT xp FROM levels WHERE user = ? AND guild = ?', (member.id, ctx.guild.id,))
            xp = await cursor.fetchone()
            await cursor.execute('SELECT level FROM levels WHERE user = ? AND guild = ?', (member.id, ctx.guild.id,))
            level = await cursor.fetchone()

            if not xp or not level:
                await cursor.execute('INSERT INTO levels (level, xp, user, guild) VALUES (?, ?, ?, ?)', (0, 0, member.id, ctx.guild.id,))
            await bot.db.commit()
            
            try:
                xp = xp[0]
                level = level[0]
            except TypeError:
                xp = 0
                level = 0
        
        embed = nextcord.Embed(title=f"{member}'s Level", color=nextcord.Color.green())
        embed.add_field(name="Level:", value=f"{level}", inline=False)
        embed.add_field(name="XP:", value=f"{xp}", inline=False)

        embed.timestamp = datetime.datetime.now()
        embed.set_footer(text = "SherBot", icon_url = "https://cdn.discordapp.com/attachments/1031828036422733825/1044698179179909290/abitgreener.png")

        await ctx.send(embed=embed)
        print("Command executed successfully.")

def setup(bot):
    bot.add_cog(LevelSystem(bot))

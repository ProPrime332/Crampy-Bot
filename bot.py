import discord
from discord.ext import commands
from discord.ext.commands.errors import CheckFailure
from config import TOKEN


bot = commands.Bot(command_prefix='.')

bot.load_extension('cogs.coms')

@bot.event
async def on_ready():
    print('Sup noob.')

bot.run(TOKEN)
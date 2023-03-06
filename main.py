import random, discord,os
#RANDOM allows the bot to generate random proceedings
from discord.ext import commands
TOKEN = os.getenv["token"]
client = commands.Bot(command_prefix )
client.run(TOKEN)
import discord
import random
from discord import Intents
from discord.ext import commands


intents = Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents )

#@bot.event
#async def on_ready():
#   channel = bot.get_channel(936689223170416691)
#   await channel.send('I have been sent to monitor and judge. Contact will be limited during The Coverage.')

@bot.event
async def on_message(message):
  
  if message.author.display_name != "Coverage Monitor":
    if random.randint(1, 40) == 12:
        msg = ('COVERAGE JUDGEMENT ASSIGNED: ' + message.author.display_name + '. Your score is being assessed. Behave accordingly.').format(message)
        await message.channel.send(msg)
  
  await bot.process_commands(message)

bot.run('TOKEN')
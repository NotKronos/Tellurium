import discord

from discord.ext import commands

# Intents, some new discord shit that I hate

intents = discord.Intents.all()
intents.message_content = True
intents.typing = True
intents.presences = True

client = commands.Bot(command_prefix=".", intents = intents)

# Settings

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')




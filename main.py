import discord

from discord.ext import commands

import config

bot_config: config = config.Config(config)

# Intents, some new discord shit that I hate

intents = discord.Intents.all()
intents.message_content = True
intents.typing = True
intents.presences = True

client = commands.Bot(command_prefix=".", intents=intents)

f = open("token", "r")
token = f.read()
f.close()

# Settings


@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

@client.command(name="prefix")
async def prefix(ctx):
    if ctx.message.author.guild_permissions.administrator:
        client.command_prefix = bot_config.prefix
        print("new prefix is: " + bot_config.prefix)

client.run(token)
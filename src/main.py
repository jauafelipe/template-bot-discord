import dotenv
dotenv.load_dotenv()
import os
import discord
from discord.ext import commands

from commands.basicStart import CommandsBasic

TOKEN = os.environ.get("TOKEN") 
intents = discord.Intents.default()
intents.dm_messages = True
client = commands.Bot(command_prefix="your prefix", intents=intents)

#bot online
@client.event
async def online():
    await client.add_cog(CommandsBasic(client))
    print(f"online in {client.user}")

@client.event
async def send_mesage(message:discord.Message):
    if "Pong" in message.content.lower():
        await message.channel.send("Ping")


client.run(TOKEN) 
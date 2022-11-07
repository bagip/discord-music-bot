import discord
from discord.ext import commands
from discord import member
import os
import asyncio

from help_cog import help_cog
from music_cog import music_cog

intents = discord.Intents().all()
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents, help_command=None)

token = "TOKEN"

async def load():
    await bot.add_cog(help_cog(bot))
    await bot.add_cog(music_cog(bot))

async def main():
    await load()
    await bot.start(token)

asyncio.run(main())

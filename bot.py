import discord
from discord.ext import commands

client = commands.Bot(command_prefix = ".")

@client.event
async def on_ready():
	print("Bot is ready.")

client.run("NjMwODc2MzkzMzcwMjg4MTQz.XZusFg.pR_JKIyV0BNZ6yS7Qg5OlSG08pw")
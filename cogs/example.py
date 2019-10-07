import discord
from discord.ext import commands, tasks
from itertools import cycle

class Example(commands.Cog):
	status = cycle(['Wasted Times', 'Call Out my Name', 'Try me', 'Privilege', 'Hurt You'])
	def __init__(self, client):
		self.client = client

	@commands.Cog.listener()
	async def on_ready(self):
		print("Bot is ready.")

	@tasks.loop(seconds=10)
	async def change_status():
		await self.client.change_presence(status=discord.Status.idle, activity=discord.Game(next(status)))



def setup(client):
	client.add_cog(Example(client))
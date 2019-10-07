import discord
import random
from discord.ext import commands


client = commands.Bot(command_prefix = ".")

@client.event
async def on_ready():
	print("Bot is ready.")

@client.event
async def on_member_join(member, ctx):
	await ctx.send(f"{member}, you made it! Welcome to the party. :)")

@client.event
async def on_memeber_remove(member, ctx):
	await ctx.send(f"Oh no! {member} has left the party. Was it something I said? :(")

@client.command()
async def ping(ctx):
	await ctx.send(f"Pong! {round(client.latency*1000)}")

@client.command()
async def clear(ctx, amount=5):
	await ctx.channel.purge(limit=amount)

@client.command()
async def kick(ctx, member : discord.Member, *, reason=None):
	await member.kick(reason=reason)

@client.command()
async def ban(ctx, member : discord.Member, *, reason=None):
	await member.ban(reason=reason)

client.run("NjMwODc2MzkzMzcwMjg4MTQz.XZuviQ.1n7uJusnO4prRsFwSHtMvzrBw2I")



#Optional Not-In-Use Commands
# @client.command(aliases = ['8ball', '8'])
# async def _8ball(ctx, *, question):
# 	responses = ['It is certain', 'It is decidedly so', 'Without a doubt', 'Yes, definitely',
# 				 'You may rely on it', 'As I see it, yes', 'Most likely', 'Outlook good',
# 				 'Signs point to yes', 'Yes', 'Reply hazy, try again', 'Ask again later',
# 				 'Better not tell you now', 'Cannot predict now', 'Concentrate and ask again',
# 				 "Don't bet on it", 'My reply is no', 'My sources say no', 'Outlook not so good',
# 				 'Very doubtful']
# 	await ctx.send(f"Question: {question}\n Answer: {random.choice(responses)}")
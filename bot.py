import discord
import random
import os
from discord.ext import commands, tasks
from itertools import cycle


client = commands.Bot(command_prefix = ".")
status = cycle(['Wasted Times', 'Call Out My Name', 'Try Me', 'Privilege', 'Hurt You'])

def admin_check(ctx):
	return ctx.author.id == 345033351532380160

#Events
@client.event
async def on_ready():
	change_status.start()

@client.event
async def on_member_join(member, ctx):
	await ctx.send(f"{member}, you made it! Welcome to the party. :)")

@client.event
async def on_member_remove(member, ctx):
	await ctx.send(f"Oh no! {member} has left the party. Was it something I said? :(")

@client.event
async def on_command_error(ctx, error):
	if isinstance(error, commands.MissingRequiredArgument):
		await ctx.send("Please pass in all required arguments.")

@client.event
async def on_command_error(ctx, error):
	if isinstance(error, commands.CommandNotFound):
		await ctx.send("Command was not found. Please try again.")

#Commands
@client.command()
async def ping(ctx):
	await ctx.send(f"Pong! {round(client.latency*1000)}")

@client.command()
async def clear(ctx, amount=5):
	await ctx.channel.purge(limit=amount)

@client.command()
@commands.has_permissions(administrator=True)
async def kick(ctx, member : discord.Member, *, reason=None):
	await member.kick(reason=reason)

@client.command()
@commands.check(admin_check)
async def ban(ctx, member : discord.Member, *, reason=None):
	await member.ban(reason=reason)

@client.command()
@commands.check(admin_check)
async def unban(ctx, *, member, reason=None):
	banned_users = await ctx.guild.bans()
	member_name, member_discriminator = member.split("#")

	for ban_entry in banned_users:
		user = ban_entry.user

		if(user.name, user.discriminator) == (member_name, member_discriminator):
			await ctx.guild.unban(user)
			await ctx.send(f"Unbanned {user.mention}")
			return

@client.command()
async def load(ctx, extension):
	client.load_extension(f"cogs.{extension}")

@client.command()
async def unload(ctx, extension):
	client.unload_extension(f"cogs.{extension}")

for filename in os.listdir("./cogs"):
	if filename.endswith('.py'):
		client.load_extension(f"cogs.{filename[:-3]}")


#Tasks
@tasks.loop(seconds=60)
async def change_status():
	await client.change_presence(status=discord.Status.idle, activity=discord.Game(next(status)))

client.run("NjMwODc2MzkzMzcwMjg4MTQz.XZu6rQ.9rD9ca-Wx3MqImvCQ3WZKBt1TIs")



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
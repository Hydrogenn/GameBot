import discord
from discord.ext import commands
import asyncio
import games
	
	
class Game_Manager:
	"""Manages games for the bot across servers and channels."""
	
	def __init__(self, bot):
		self.bot = bot #the bot running this cog.
		self.game_rooms = {} #the channels that are running a game, mapped to their respective game.
		self.games = [] #the games to choose between, chosen at startup
		
		self.games.extend([games.Base, games.Random_Winner])
	
	def __getitem__(self, channel):
		if channel not in self.channels.keys():
			self.channels[channel] = Game(channels[channel])
		return self.channels[channel]
	
	def getchannel(self, user):
		if user not in self.usercache.keys():
			return None
		return self.usercache[user]
	
	async def on_reaction_add(self, reaction, user):
		if user.bot:
			return
		for channel in self.channels:
			if reaction.message.id == self.channels[channel].menu.id:
				emoji = reaction.emoji
				if emoji == "▶":
					await self.channels[channel].start_game()
				elif emoji == "🔀":
					await self.channels[channel].start_game()
				else:
					self.channels[channel].add_participant(user)
					await self.channels[channel].vote(int(str(reaction.emoji)[0]))
	
	async def on_reaction_remove(self, reaction, user):
		if user.bot:
			return
		for channel in self.channels:
			if reaction.message.id == self.channels[channel].menu.id:
				await self.channels[channel].vote(int(str(reaction.emoji)[0]), -1)
	
	@commands.command(pass_context=True)
	async def game(self, ctx):
		"""Takes over the channel and turns it into a gaming one!"""
		
		self.channels[ctx.message.channel] = GameHandler(self, ctx.message.channel)
		await self[ctx.message.channel].generate_menu(True)
	

def setup(bot):
	game_manager = Game_Manager(bot)
	bot.add_cog(game_manager)

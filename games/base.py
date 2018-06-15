"""
Deleting this class will prevent GameBot from running properly.
"""

from abc import ABC

class Participant:
	"""A player participating in a game. This is connected to a game_manager, not a game."""
	def __init__(self, user, channel):
		self.user = user
		self.channel = channel

class Base:
	"""This is a base game for all existing games. Import and extend it."""
	
	name = "Generic Game"
	min_players = 1
	
	def __init__(self, game_manager):
		self.game_manager = game_manager
		self.participants = None
	
	async def start(self, participants):
		mess = []
		mess.append("The game is very boring because it does not exist yet.")
		mess = "\n".join(mess)
		
		em = discord.Embed(title='Welcome to the game.', description=mess, colour=0x808080)
		
		await self.game_manager.update_menu(em)
		
		self.participants = participants
		
		for participant in self.participants:
			pass
			
	def remove(self, participant):
		self.game_manager.say("Someone left the game, which is illegal. We're ending this.")
		self.end()
	
	async def end(self):
		await self.game_manager.reset()
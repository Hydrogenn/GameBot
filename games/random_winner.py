'''
This is a test game to demonstrate basic capabilities.
Feel free to remove this.
'''

import base
import random

class Random_Winner(Base):
	"""Picks a random winner from all participants."""
	
	name = "The Random Winner Game!"
	min_players = 1
	
	def __init__(self, game_manager):
		Base.__init__(self, game_manager)
	
	async def start(self, participants):
		self.menu = Menu()
		winner = random.choice(participants)
		mess = []
		mess.append("Congratulations! " + winner.user.mention + " wins the random winner game!")
		mess = "\n".join(mess)
		
		em = discord.Embed(title='Winner Time!', description=mess, colour=0xffff80)
		
		await self.game_manager.update_menu(em)
		await self.end()
	
	async def end(self):
		await self.game_manager.say("Game End.")
		await self.game_manager.reset()
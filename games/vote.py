'''
Do not delete this, the game manager is dependent on it.
This looks through all other games available, gets user votes, and picks between them.
'''

import base

os.listdir()

class Vote_Item:
	def __init__(self, game):
		self.game = game
		self.votes = 0

class Vote(Base):
	
	name = "Vote"
	min_players = 0
	games = []
	
	def __init__(self, game_bot, channel):
		self.game_bot = game_bot
		self.channel = channel
		self.participants = []
		self.votes = []
		self.games = []
		self.game = None
		self.menu = None
	
	
	async def vote(self, index, value = 1):
		self.votes[index].votes += value
		if self.votes[index].votes >= self.front_runner() and self.votes[index].votes >= self.votes[index].game.min_players:
			self.games.append(self.votes[index].game)
		elif self.votes[index].game in self.games:
			self.games.remove(self.votes[index].game)
		await self.update_embed()
		
	def front_runner(self):
		most_votes = 0
		for vote in self.votes:
			most_votes = max(most_votes, vote.votes)
		return most_votes
	
	async def start_game(self):
		self.running = True
		self.game = random.choice(self.games)
		await self.game.start(self.participants)
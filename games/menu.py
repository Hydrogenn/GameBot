


class Menu:
	"""This is the embedded window that most games use, because it looks nice and can contain images."""
	
	def __init__(self, game):
		self.game = game
		self.message = None
		
	async def generate_menu(self, first_time):
		for game in self.game_bot.playable_games:
			self.votes.append(Vote(game(self)))
		if first_time:
			self.menu = await self.say("***DID SOMEBODY SAY GAME?!***")
		else:
			self.menu = await self.say("Discord told me this message had to be here. It'll get fixed... eventually.")
		await self.update_embed()
		await self.game_bot.bot.add_reaction(self.menu, 'ðŸ”');
		for index, vote in enumerate(self.votes):
			await self.game_bot.bot.add_reaction(self.menu, str(index) + 'âƒ£')
	
	async def update_embed(self):
		message = []
		message.append("React to pick a game. Hit play to start the most popular option!")
		message.append("ðŸ” View Admin Page")
		for index, vote in enumerate(self.votes):
			message.append(str(index) + "âƒ£ **(" + str(vote.votes) + "/" + str(vote.game.min_players) + ")** " + str(vote.game.name))
		if len(self.games) == 0:
			message.append("ðŸš« *Not enough players.*")
			await self.game_bot.bot.remove_reaction(self.menu, "ðŸ”€", self.game_bot.bot.user)
			await self.game_bot.bot.remove_reaction(self.menu, "â–¶", self.game_bot.bot.user)
		elif len(self.games) == 1:
			message.append("â–¶ **Play " + self.games[0].name + "**")
			await self.game_bot.bot.add_reaction(self.menu, "â–¶")
			await self.game_bot.bot.remove_reaction(self.menu, "ðŸ”€", self.game_bot.bot.user)
		else:
			game_names = []
			for game in self.games:
				game_names.append(game.name)
			message.append("ðŸ”€ **Play one of " + ", ".join(game_names) + " through random selection**")
			await self.game_bot.bot.add_reaction(self.menu, "ðŸ”€")
			await self.game_bot.bot.remove_reaction(self.menu, "â–¶", self.game_bot.bot.user)
		message = "\n".join(message)
		embed = discord.Embed(title='Welcome to the game.', description=message, colour=0x808080)
		await self.game_bot.bot.edit_message(self.menu, embed = embed)
	
	async def update_menu(self, menu):
		await self.game_bot.bot.edit_message(self.menu, embed = menu)
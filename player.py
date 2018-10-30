#Monte Roybal
#Player Object Class

class Player(object):

	def __init__(self,name="",wins=0,losses=0):
        #Attributes for player's names, wins and losses
		self.name = name
		self.wins = wins
		self.losses = losses

		self.winner = False#winner state defaulted to False

	def __str__(self):
		print "{}".format(self.name)
    #Set player's name
	def set_name(self,name):
		self.name = name 
    #Increment wins
	def add_win(self):
		self.wins += 1
    #Increment losses
	def add_loss(self):
		self.losses += 1
    #Change winner state to True
	def declare_winner(self):
		self.winner = True

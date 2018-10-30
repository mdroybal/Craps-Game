#Monte Roybal
#Craps Table Player Object Class
from player import *
from dice import *
from ledger import *

class Craps_Player(object):
    #Inherit
    def __init__(self):
        #Dice objects
        self.dye_1 = Dice()
        self.dye_2 = Dice()
        self.dice = [self.dye_1,self.dye_2]#list of dice objects
        #Player object
        self.player = Player()
        self.ledger = Ledger()
    #Set player name with player class set name function
    def player_name(self,name):
        self.player.set_name(name)
    #Add to player's stack with ledger class increase balance function 
    def stack_up(self,amount):
        self.ledger.increase_balance(amount)
    #Subtract with player's stack with ledger class decrease balance function  
    def place_bet(self,amount):
        self.ledger.decrease_balance(amount)
    #Return player's money balance through ledger class balance function
    def get_balance(self):
        return self.ledger.admin_get_balance()
    #Add a loss with player class add loss function        
    def loss(self):    
        self.player.add_loss()
    #Add a win from player class add win function
    def win(self):
        self.player.add_win()
    #Generate random dice integer values with dice class roll function
    def roll_dice(self):
        for i in self.dice:
            i.roll()
    #Sum dice objects with object/dice classes overridden sum function
    def sum_dice(self):
        return sum(self.dice)
    #Print dice list integer values
    def show_dice_value(self):
        for i in self.dice:
            print i.dice
    #Display dice emojis with dice class get dice function
    def display_dice(self):
        for i in self.dice:
            i.get_dice()

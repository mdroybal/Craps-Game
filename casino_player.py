#Monte Roybal
#Casino Table Player Object Class

import random
from ledger import *
from player import *
from bank_account import *

class Casino_Player(Player):

    def __init__(self,account=0):        
        super(Casino_Player,self).__init__()#Inheritance of Player object
        self.new_account = account
        self.ledger = Ledger()
    #Add bank accounts for each player        
    def add_bank_accounts(self,name):
        print "Please create a bank account,"
        self.new_account = Bank_Account()
        print "Your Default PIN: {}".format(self.new_account.admin_get_pin())
        self.new_account.set_pin()
        self.new_account.set_name(name)
        self.new_account.make_deposit() 
        rand_num = random.randint(100000,999999)
        self.new_account.set_acct_numb(rand_num)
        self.new_account.first_login()
        print self.new_account
        


    def get_account(self):
        return self.new_account



    #Add to player's stack with ledger class increase balance function 
    def stack_up(self,amount):
        self.ledger.increase_balance(amount)
    #Subtract with player's stack with ledger class decrease balance function  
    def place_bet(self,amount):
        self.ledger.decrease_balance(amount)
    #Return player's money balance through ledger class balance function
    def get_balance(self):
        return self.ledger.admin_get_balance()
        
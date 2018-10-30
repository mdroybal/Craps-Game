#Monte Roybal
#CS_515
#Virtual Craps Dice Game

import sys,random
from casino_player import *
from dice import *

#Craps Table Object Class       
class Craps_Table(object):

    def __init__(self,player="",account=""):
        self.players = []#list of players
        self.bank_accounts = []#list of bank accounts
        self.current_player = player#current player attribute
        self.current_account = account#current bank account attribute
        #Dice objects
        self.dye_1 = Dice()
        self.dye_2 = Dice()
        self.dice = [self.dye_1,self.dye_2]#list of dice objects
    #Add N number of players from user input
    def add_players(self): 
        global new_player,num_players
        num_players = input("Welcome to Virtual Craps.....\nHow Many Players will be Playing today? ")
        print "\nEnter your Names and Amount of Money to Sit Down With!"
        i = 1
        for i in range(1,num_players+1):
            name = raw_input("\n_______PLAYER {}_______\nPlease enter your name: ".format(i))
            new_player = Casino_Player()#Player object
            new_player.set_name(name)
            new_player.add_bank_accounts(name)
            self.bank_accounts.append(new_player.get_account()) 
            print "\nAdd chips to your Stack to Play"
            amount = self.bank_withdraw(new_player.get_account())
            new_player.stack_up(amount)
            print "\nYour stack is now ${}".format(new_player.get_balance())
            self.players.append(new_player)
    #Retrieve current player's name
    def get_current_player_name(self):
        return self.current_player.name
    #Set first player
    def set_first_player(self):
        self.current_player = self.players[0]
    #Set first player bank account
    def set_account(self):
        self.current_account = self.bank_accounts[0]
    #Rotate through players list to next player
    def set_next_player(self):   
        for i,j in enumerate(self.players):
            if j == self.current_player:
                self.current_player = self.players[(i+1)%len(self.players)]
                break
    #Rotate through bank accounts list to next player's bank account
    def set_next_account(self):   
        for i,j in enumerate(self.bank_accounts):
            if j == self.current_account:
                self.current_account = self.bank_accounts[(i+1)%len(self.bank_accounts)]
                break
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
    #Pay out players based on bet type and keep track of losses and wins
    def pay_out(self,msg,amount,BET):
        if BET.upper() == "PASS":
            Main_Table.current_player.stack_up(amount)
            bal = Main_Table.current_player.get_balance()                  
            Main_Table.current_player.add_win()
            print msg
        elif BET.upper() == "DONT PASS":
            Main_Table.current_player.add_loss()
            print msg
        bal = Main_Table.current_player.get_balance()    
        print "Stack is now ${}".format(bal) 
    #Withdraw money from players bank account
    def bank_withdraw(self,obj):
        try:
            obj.login()
            amount = obj.make_withdraw()
            obj.logout()
        except TypeError:
            Main_Table.set_next_player()
            Main_Table.set_next_account()
            main()
        return amount 
    #Allow players to place a bet if they have enough money in their stack
    def bet_amt(self):
        Bet = input("\nBetting {} Line\nHow Much would You Like to Bet: $".format(bet_type))
        Bal = Main_Table.current_player.get_balance()
        if Bet > Bal:
            if Bet == exit or Bet == quit:
                self.winner()
            else:
                print "Your bet Exceeds your Stack" 
                return "Exceeds"
        else:
            return Bet
    #Check if player has a stack with no money and prompt them to withdraw money
    def zero_balance(self):
        if start_bal == 0:#check if player's stack is greater than $0
            print "{}, you have No Money in Your Stack!\nMake a Withdrawal to Play!".format(Main_Table.get_current_player_name())
            amount = Main_Table.bank_withdraw(Main_Table.current_account)
            if amount > 0:
                Main_Table.current_player.stack_up(amount)
                Main_Table.current_player.get_balance()
                print "\nYour stack is now ${}".format(Main_Table.current_player.get_balance())
            else:
                self.zero_balance()
    #Print out player wins and losses statistics if string is entered during bet    
    def winner(self):
        all_wins = []
        for i in self.players:
            all_wins.append(i.wins)
        largest_win = max(all_wins)
        for i in self.players:
            if i.wins == largest_win:
                i.declare_winner()
                if i.winner == True:
                    print "\n{} Had the Most Wins with {}\n".format(i.name,largest_win)
            stats = "{} had {} Wins and {} Losses".format(i.name,i.wins,i.losses)
            print stats
        sys.exit("\nThank You for playing Monte's Virtual Craps Dice Game, See you next time! GOODBYE")
    #Players first roll of dice with bet type selection and amount to gamble
    def player_turn(self):
        global bet,bet_type,start_bal,PASS,DONT_PASS
        PASS = "Pass"
        DONT_PASS = "Dont Pass"
        Main_Table.roll_dice()
        start_bal = Main_Table.current_player.get_balance()
        self.zero_balance()
        start_bal = Main_Table.current_player.get_balance()
        print "\n{}'s turn,\nStack is ${}\n".format(Main_Table.get_current_player_name(),start_bal)
        bet_type = raw_input("Choose your bet:     (1)Pass     OR     (2)Dont Pass: ")
        if bet_type.upper() == "1":
            bet_type = PASS
        elif bet_type.upper() == "2":
            bet_type = DONT_PASS        
        bet = self.bet_amt()
        if bet == "Exceeds":
            Main_Table.player_turn()
            point = Main_Table.sum_dice()
            return point
        else:
            bet_type.upper()
            PASS.upper()
            DONT_PASS.upper()
            Main_Table.current_player.place_bet(bet)
            player_action = ""
            point = Main_Table.sum_dice()
            return point
    #Print out what player rolled
    def point_roll(self,dye):
        rolls = "\n{} rolled {}".format(Main_Table.get_current_player_name(),dye)
        print rolls
        Main_Table.display_dice()
    #Allow player to roll again to attempt their point if they did not crap out or get a 7/11
    def roll_again(self,dye):
        amount_won = bet * 2
        got_point = "\n{} wins ${} with the {} point!".format(Main_Table.get_current_player_name(),bet,dye)
        no_go_point = "\n{} loses ${} with the {} point".format(Main_Table.get_current_player_name(),bet,dye)
        seven_out = "\n{} lost ${} with a seven out".format(Main_Table.get_current_player_name(),bet)
        seven_on = "\n{} won ${}, but got a seven out!".format(Main_Table.get_current_player_name(),bet)    
        raw_input("Hit ENTER to roll")
        Main_Table.roll_dice()
        point_attempt = Main_Table.sum_dice()
        Main_Table.point_roll(point_attempt)
        if point_attempt == dye:#conditional to catch if player got their point
            if bet_type == PASS:
                Main_Table.pay_out(got_point,amount_won,PASS)
            elif bet_type == DONT_PASS:
                Main_Table.pay_out(no_go_point,amount_won,DONT_PASS)
            main()
        elif point_attempt == 7:#conditional to catch if player got a seven out
            if bet_type == DONT_PASS:
                Main_Table.pay_out(seven_on,amount_won,PASS)
            elif bet_type == PASS:
                Main_Table.pay_out(seven_out,amount_won,DONT_PASS)
            Main_Table.set_next_player()
            Main_Table.set_next_account()
            main()
        else:
            Main_Table.roll_again(dye)

#Main Function
if __name__ == "__main__":
    Main_Table = Craps_Table()#Craps Table Object
    Main_Table.add_players()
    Main_Table.set_first_player()
    Main_Table.set_account()
    def main():
        try:#try player turn if proper data is input
            point = Main_Table.player_turn()
        except TypeError:#except a Type Error to allow player to input string during bet to exit
            Main_Table.winner()
        #Enter while loop if player does not crap out or get a 7/11
        while point != 7 and point != 11 and point != 2 and point != 3 and point != 12:
            Main_Table.point_roll(point)
            Main_Table.roll_again(point)
                  
        Main_Table.point_roll(point)
        amount_won = bet * 2
        if point == 7 or point == 11:#Conditional to catch a 7/11
            natural = "\n{} wins ${} with the {} natural!".format(Main_Table.get_current_player_name(),bet,point)
            non_natural = "\n{} loses ${} with the {} natural".format(Main_Table.get_current_player_name(),bet,point)
            if bet_type == PASS:
                Main_Table.pay_out(natural,amount_won,PASS)
            elif bet_type == DONT_PASS:
                Main_Table.pay_out(non_natural,amount_won,DONT_PASS)
            main()
   
        if point == 2 or point == 3 or point == 12:#Conditional to catch a crap out
            crapped = "\n{}, you crapped out with a {} and lost ${}".format(Main_Table.get_current_player_name(),point,bet)
            non_crapped = "\n{}, you crapped out with a {}, but won ${}!".format(Main_Table.get_current_player_name(),point,bet)
            if bet_type == DONT_PASS:
                Main_Table.pay_out(non_crapped,amount_won,PASS)
            elif bet_type == PASS:
                Main_Table.pay_out(crapped,amount_won,DONT_PASS)                
            main()
main()
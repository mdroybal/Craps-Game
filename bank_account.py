#Monte Roybal
#Bank Account Object Class

from ledger import *

class Bank_Account(Ledger):
    def __init__(self,owner_name="",pin="0000",acct_numb=00000000):
        self.__owner_name = owner_name
        self.__pin = pin
        self.__acct_numb = acct_numb
        super(Bank_Account,self).__init__()#Inheritance of Ledger object

        self.__is_logged_in = False#is logged in state defaulted to False

    def __str__(self):
        if self.__is_logged_in == True:
            return "\nAccount owner's name: {}\nPIN: {}\nAccount Number: {}\nBalance: ${}".format(self.__owner_name,self.__pin,self.__acct_numb,self.admin_get_balance())
        else:
            return "\nPlease enter your PIN before you can see your information!\n"
    #Set a custom PIN
    def set_pin(self):
        if self.__is_logged_in == True:
            user_set_pin = raw_input("\nPlease choose a four digit PIN: ")
            if len(user_set_pin) == 4:
                self.__pin = user_set_pin
                self.logout()
            else:
                print "\nPlease make sure PIN is only 4 numbers!"
                self.set_pin()
        else:
            print "\nPlease enter your CURRENT PIN and then change it\n"
            self.login()
            self.set_pin()
    #User input for PIN
    def get_pin(self):
        user_pin =  raw_input("Enter PIN: ")
        return user_pin
    #Change is logged in to True state
    def first_login(self):
        self.__is_logged_in = True    
    #Login to account
    def login(self):
        Pin = self.get_pin()
        if self.__pin == Pin:
            if self.__is_logged_in == False:
                self.__is_logged_in = True
        else:
            print "#################\n#  Wrong PIN!!  #\n#################"
            self.logout()
            self.login()
    #Logout of account
    def logout(self):
        self.__is_logged_in = False
    #Set owner name
    def set_name(self,name):
        self.__owner_name = name
    #Retrieve owner name   
    def get_name(self):
        return self.__owner_name
    #Set account number
    def set_acct_numb(self,num):
        self.__acct_numb = num
    #Retrieve PIN
    def admin_get_pin(self):
        return self.__pin
    #Get balance if logged in to account
    def get_balance(self):
        if self.__is_logged_in == True:
            print "Your account balance is ${}".format(self.admin_get_balance())
            self.logout()
        else:
            self.login()
            self.get_balance()
    #Make withdraw from account 
    def make_withdraw(self):
        if self.__is_logged_in == True:
            withdraw = input("How much would you like to withdraw: \n")
            if withdraw <= self.admin_get_balance(): 
                self.decrease_balance(withdraw)
                print "You have just withdrawn ${}".format(withdraw)
                print "Your account balance is now ${}".format(self.admin_get_balance())
                self.logout()
                return withdraw
            else:
                minus = withdraw - self.admin_get_balance()
                print "Your account balance is only ${}\nYou Cannot Withdraw ${} because it Exceeds your balance by ${}!".format(self.admin_get_balance(),withdraw,(minus))
                return 0
                self.make_withdraw()
        else:
            self.login()
            self.make_withdraw()
    #Make deposit to account
    def make_deposit(self):
        if self.__is_logged_in == True:
            deposit = input("How much would you like to deposit: ")
            self.increase_balance(deposit)
            print "You have just deposited ${}".format(deposit)
            print "Your account balance is now ${}".format(self.admin_get_balance())
            self.logout()
        else:
            self.login()
            self.make_deposit()

#Monte Roybal
#Ledger Object Class

class Ledger(object):

	def __init__(self,balance=0.00):
		self.__balance = balance#ledger balance attribute defaulted to 0
    #Add operator overide to add objects
	def __add__(self,other):
	    total = self.__balance + other
	    return Ledger(total)
	#Sum function overide to sum objects
	def __radd__(self,other):
	    total = self.__balance + other
	    return total
    #Return balance
	def admin_get_balance(self):
	    return self.__balance
	#Decrement balance      
	def decrease_balance(self,amount):
	    self.__balance -= amount
    #Increment balance
	def increase_balance(self,amount):
	    self.__balance += amount
#Monte Roybal
#Dice Object Class

import random

class Dice(object):

    def __init__(self,dice =0):
        self.dice = dice#dice integer value attribute

    def __str__(self):
        return "{}".format(self.dice)
    #Add operator overide to add objects
    def __add__(self,other):
        roll = self.dice + other.dice
        return Dice(roll)
    #Sum function overide to sum objects
    def __radd__(self,other):
        total = self.dice + other
        return total
    #Randomly generate dice integer values 1 through 6
    def roll(self):
        self.dice = random.randint(1,6)
    #Construct dice emojis based on dice integer value
    def get_dice(self):
        top = "___________\n|         |\n"
        middle =  "|    0    |\n"
        blank = "|         |\n"
        bottom = "|_________|\n"
        left_single = "|  0      |\n"
        right_single = "|      0  |\n"
        two = "|  0   0  |\n"
        three = "|  0 0 0  |\n"   
        if self.dice == 1:
            print top + blank + middle + blank + bottom
        if self.dice == 2:
            print top + left_single + blank + right_single + bottom
        if self.dice == 3:
            print top + left_single + middle + right_single + bottom
        if self.dice == 4:
            print top + two + blank + two + bottom
        if self.dice == 5:
            print top + two + middle + two + bottom
        if self.dice == 6:
            print top + three + blank + three + bottom

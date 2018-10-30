#Monte Roybal
#Virtual Craps Dice Game 

README

This dice craps game was designed with an object-oriented approach that was intended to harness as much functionality from inherited or imported classes as possible. The functionality from one class object to another was not intended to be redundant and create duplicate functions, although many functions were required to either wrap functionality from other classes or access private attributes. 

The flow and functionality of the objects are as follows:

1. The dice class generates a random dice integer value, constructs the dice emoji, and overrides the add and reverse add object class functions to allow the addition or summation of objects. Dice class inherits from the object class. 

2. The player class allows a player object with a name, count of losses and wins and a winner state to be generated. Player class inherits from the object class.

3. The ledger class keeps track of a private balance attribute which may be incremented, decremented or retrieved. It also overrides the add and reverse add object class functions to allow the addition or summation of objects. Ledger class inherits from the object class also.

4. The craps player class brings the player, dice and ledger classes together. This allows the generation of a craps player object that utilizes most of the player, dice and ledger class imported functionality for the modeling of a craps player. Craps player class inherits from the object class.

5. The craps game class inherits directly from the craps player class to allow the simulation of a craps game. The craps game class also utilizes functionality from the bank account class to generate a bank account object for each player. Through the bank account object, the craps player is required to create an account. The player may withdraw from their account to add to their stack within the game to enable gambling. The craps game class entails all the craps rules and follows them throughout the simulation. The pass and don’t pass line betting methods are also implemented to allow players to choose their betting style along with desired gamble amount. 

The two Python module imports are sys and random. 
The Python Version utilized is Python 2.7.12

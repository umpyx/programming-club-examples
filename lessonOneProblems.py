# Fix this program so it executes correctly, there are plenty of syntax errors!
import random
variableOne -= 3
variableTwo = 10
print(variableOne)
variableThree = variableOne + variabletwo
if variableThree < random.randint(5.20)
	print("Hello!)
else:
print("Too small :(")
	exit()

# You're making a calculator, and you want to make sure the user does not input any characters,
# because it crashes the program when the input is turned into an integer using the int() function
# you can use the isdigit() function in order to test if an input contains digits

print("Input two numbers")
numberOne = input("Please input the first number")
#implement your solution here!
numberTwo = input("Please input the second number")
#implement your solution here!

print(f"Your output is {numberOne} + {numberTwo} = {numberOne + numberTwo}")
#Unfortunately this calculator can only do addition

#Your friend is making a game, and he has no idea how to ask for the player's input to make a decision
#Help him out!

import random

playerHealth = 100
enemyHealth = 100
gameRunning = True
while gameRunning == True:
	print(f"Player health: {playerHealth}")
	print(f"Enemy health: {enemyHealth}")
	playerBlocking = False
	print("You can either punch, block, or heal, what would you like to do?")
	
	#implement your solution here!
	if punch:
		enemyHealth -= 15
	elif block:
		playerBlocking = True
	elif heal:
		playerHealth += 10
	
	#enemy attacks
	if random.randint(0,3) == 2:
		print("Enemy Heals!")
		enemyHealth += 10
	else:
		print("Enemy Attacks!")
		if playerBlocking == True:
			playerHealth -= 5
		else:
			playerHealth -= 15
	
	if playerHealth < 1:
		print("Player has lost!")
		exit()
	elif enemyHealth < 1:
		print("Player has won!")
		exit()


# WEEKLY PROJECT
# You're building a menu system for your local grocery store. Display the prices and names of each item,
# Allow the customer to select which item they want using the input() function, and tell them the price
# of their selection; if you are able to use loops, use that as well and allow them to select multiple items



		

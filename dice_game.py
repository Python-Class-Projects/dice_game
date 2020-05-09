# Importing random module so that the file has access to random.randint
import random

print("\nHello. Welcome to my dice game.")

play_again = "y"

while play_again == "y":

	#Initializing variables inside the loop so that for every iteration, the data will be restarted and displayed properly.
	dice_roll = [0,0]
	dice_total = 0
	input("\nPress enter to roll two dices.\n")

	#For loop to iterate through the dice_roll list elements and properly add the values of each dice roll onto the dice_total variable. 
	for i in dice_roll:

		i = random.randint(1,6) 
		dice_total = dice_total + i
		print(f"You rolled {i}.")

	#Conditional statement so that if the user rolls a losing/winning number on the first roll, 
	#the user is prompted with a losing message and is asked to play again. If the user is victorious, then user receives a victory message and an option to play again.
	#If the user does not roll a winning/losing number on the first roll, then on the else statement, the user receives a target and is asked to roll a dice again.
	if (dice_total == 2 or dice_total == 3 or dice_total == 12):
		print(f"you lost for rolling a total of: {dice_total} on your first try.")
		play_again = input("\nDo you want to play again? y/n: ")
		play_again = play_again.lower()

	elif (dice_total == 7 or dice_total == 11): 
		print(f"you won for rolling a total of: {dice_total} on your first try.")
		play_again = input("\nDo you want to play again? y/n: ")
		play_again = play_again.lower()

	else:
		print(f"Your rolled a total of: {dice_total}. Your target is {dice_total}.")
		input(f"\nPress enter to roll and aim Your target: {dice_total}. Do not roll a 7!\n")
		target_value = "true"

#The else statement has an initialized variable string of "true" to indicate to the program that there is a target the user is aiming for. 

#Implementation of break keyword inside the if statements to break out of the while loop once the target is reached or the user loses and rolls a "7"
#The while loop contains a for loop to itterate through the target_roll values and obtain two roll values for the user. 
#target is equal to the dice_total that is received in the previous while loop (else statement). 
		while (target_value == "true"): 
			target = dice_total
			target_total = 0
			target_roll = [0,0]

			for i in target_roll:

				i = random.randint(1,6) 
				target_total = target_total + i
				print(f"You rolled {i}.")

			if target_total == target:
				print(f"You won for rolling {target_total}, which is equal to your target: {target}")
				play_again = input("\nDo you want to play again? y/n: ")
				play_again = play_again.lower()
				break

			elif target_total == 7:
				print(f"You lost for rolling a total of: {target_total}.")
				play_again = input("\nDo you want to play again? y/n: ")
				play_again = play_again.lower()
				break

			else:
				print(f"Your roll total is: {target_total}")
				input("\nPress enter to continue rolling.\n")

#The else statement does not have a break key word because the user needs to be inside the loop to keep on rolling.

print("\nThanks for playing!\n\nEND OF PROGRAM.\n")



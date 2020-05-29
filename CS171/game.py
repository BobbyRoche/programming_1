#Robert Roche
#Lecture A, Lab 062


import sys
import random									#imports random so we can randomize numbers and the doors
random.seed()									#uses seed to make numbers truly random

def setupDoors():								#this function sets the doors in a list and randomizes the list
     doors=['G','G','C']
     random.shuffle(doors)							#the list is returned to be used for the game
     return doors

def playerDoor():								#this function simply returns a random number 1, 2, or 3 to be used as the players door of choice
     return random.randint(1,3)

def montyDoor(doors,player_door):						#this function sets monty's door to be used for the game
     i = 0
     player_door-=1
     while i < len(doors):							#this loop goes through each door and picks one to qualify as monty's door
          if i != player_door and doors[i] == 'G':				#the door cannot be the car, and cannot be chosen by the player already.
               return i+1
          i+=1									#returns i+1 to be the actual value of the door since i starts at 0
def playRound():								#plays a round of the game, calls each function and returns whether the player won initially or if the player woud win by switching doors
     doors = setupDoors()
     player_door = playerDoor()
     monty_door = montyDoor(doors,player_door)
     if doors[player_door-1] == 'C':
          return 0
     else:
          return 1

###### main function #######
print("Welcome to Monty Hall Analysis\nEnter \'exit\' to quit.")		#opening remarks for the game
num_tests = " "
while num_tests!='exit':							#enters the loop automatically, and sets necessary variables to 0 to reset each time we run the tests.
     i=0
     stay = 0
     switch = 0
     percent_stay = 0
     percent_switch = 0
     num_tests=input("How many tests should we run?\n")				#asks the user how many test we should run
     try:									#try except makes sure the entry is an integer
          num_tests = int(num_tests)						#if it is not it checks to see if it is 'exit', if it is the program ends, if not it gives the error message and resets.
     except ValueError:
                if num_tests == 'exit':
                        continue
                print("Bad input!\nPlease enter an integer")
                continue

     while i < num_tests:							#runs the tests the proper number of times 
               result = playRound()
               if result == 0:
                    stay +=1							#if stay wins stay is increased by 1, if switch wins switch is increased by 1.
               elif result == 1:
                    switch += 1
               i+=1
     percent_stay = round(stay/num_tests,3)					#calculates the percentages rounded to 3 so we can have percentages with one decimal place
     percent_switch = round(switch/num_tests,3)
     print ("Stay Won " + str(round(percent_stay*100,3))+"%  of the time.")	#prints results and re-rounds to ensure infinite decimals are rounded as well.
     print ("Switch Won " + str(round(percent_switch*100,3))+"%  of the time.")

print("Thank you for using this program.")					#output if exit is entered
sys.exit()					
          

		
"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------

For this first project we will be using Workspaces. 

NOTE: If you strongly prefer to work locally on your own computer, you can totally do that by clicking: File -> Download Workspace in the file menu after you fork the snapshot of this workspace.

"""

import random


def start_game():
    """Psuedo-code Hints
    
    When the program starts, we want to:
    ------------------------------------
    1. Display an intro/welcome message to the player.
    2. Store a random number as the answer/solution.
    3. Continuously prompt the player for a guess.
      a. If the guess greater than the solution, display to the player "It's lower".
      b. If the guess is less than the solution, display to the player "It's higher".
    
    4. Once the guess is correct, stop looping, inform the user they "Got it"
         and show how many attempts it took them to get the correct number.
    5. Let the player know the game is ending, or something that indicates the game is over.
    
    ( You can add more features/enhancements if you'd like to. )
    """
    # write your code inside this function.
    
    print("-" * 38)
    print(" Welcome to the Number Guessing Game!")
    print("-" *38)
    
    
    # initiate highscore value 
    high_score = 0
    
    # set initial trial to zero
    trial = 0
    
    # set answer is False, the while loop will stop if the answer True
    answer = False
    
    # actual random number
    num = random.randint(1, 10)
    
    while not answer:
      trial += 1
      guess = get_input() 
      
      if guess < num:
        print("It is higher!")
      elif guess > num:
        print("It is lower!")
      else:
        # inform the user once the guess correct
        print(f"\nYou got it. It took you {trial} tries.\n")
        
        if high_score == 0:
          # set high_score equal to trial when first attempt
          high_score = trial
          
        # the high score is the least number of trials
        elif (trial < high_score):
          high_score = trial
        
        # take input whether player want to continue or not
        game = input("Do you want to continue? [y/n] : ")
        
        if game == 'y' or game == 'Y':
          # reset trial
          trial = 0
          # re-generate actual random number
          num = random.randint(1, 10)
          
          print(f"\nThe HIGHSCORE is {high_score}\n")
        else:
          answer = True
          print("\nGAME OVER!")
          print(f"\nThe HIGHSCORE is {high_score}\n")   
          
def get_input():
    # ensure input is an int number and within range 1-10
    while True:
      try :
        # take guess number
        guess = int(input("Pick a number between 1 and 10 : "))
        if (guess < 1) or (guess > 10):
          print("Try again, your number is outside the guessing range")
        else:
          break
      except:
        print("Invalid input type")
    
    return guess

    
    
if __name__ == '__main__':
    # Kick off the program by calling the start_game function.
    start_game()

import random 
import logo_guess_the_number from art
continue_game = True

chosen_number = random.randint(1, 100)
game_level = input("choos a difficulty level : 'e' for easy 'h' for hard ")
guessed_number = int(input("please guess a number between 1 and 100 :  "))


def compare():
  global guessed_number
  global continue_game
  # while chosen_number != guessed_number:  
    
  if chosen_number == guessed_number :
    return "that was correct" 
    continue_game = False
  elif chosen_number < guessed_number :
    guessed_number = int(input("too much guess a smaller one : "))
  
  elif chosen_number > guessed_number:
    guessed_number = int(input("its too low guess a biger one : "))
  else:
   print("you lose your chances")

def hard_game():
     for i in range(4):
         compare()
def easy_game():
  
    for i in range(9):
        compare()
 
def play_game():
  if game_level == "h":
     hard_game()
  elif game_level == "e":
     easy_game()
  
play_game()

import random
from art import logo
import os

play='y'

def Guess_no():
  print(logo)
  end_game=False
  no = random.randint(1, 100)
  print("Im thinking of a Number between 1 and 100")
  diff = input("Choose difficulty.Type 'easy' or 'hard': ").lower()
  guess = 5 if diff == 'hard' else 10
  while not end_game:
    print(f"You have {guess} attempts remaining to guess the number.")
    guess_no = int(input("Make a guess: "))
    if guess_no > no:
      print("Too high")
    elif guess_no < no:
      print("Too Low")
    else:
      print(f"You Got it the answer was {no}")
      end_game=True
    guess -= 1
    if guess==0:
      print(f"You exhausted your attempts Correct answer was {no}\nYou lose:(")
      end_game=True
    elif not end_game:
      print("Guess again")
    

while play=='y':
  Guess_no()
  play=input("Press 'y' to play again or any other key to exit: ")
  os.system('clear')

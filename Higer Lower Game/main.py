from art import logo,vs
from game_data import data
import random
import os

def high_low(choice1,score):
  os.system('clear')
  print(logo)
  if score>0:
    print(f"You're right! Current score: {score}")
  choice2=random.choice(data)
  while choice1==choice2:
    choice2=random.choice(data)
  print(f"Compare A: {choice1['name']}, a {choice1['description']}, from {choice1['country']}\n",vs)
  print(f"\nAgainst B: {choice2['name']}, a {choice2['description']}, from {choice2['country']}")
  select=input("Who has more followers? Type 'A' or 'B':").lower()
  if (select=='a' and choice1['follower_count']>choice2['follower_count']) or (select=='b' and choice2['follower_count']>choice1['follower_count']):
    choice1=choice2
    score+=1
    high_low(choice1,score)
  else:
    print(f"Sorry, that's wrong. Final score:{score}")
  
count=0
high_low(random.choice(data),count)  

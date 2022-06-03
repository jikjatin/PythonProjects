import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
user=int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
draw=[rock,paper,scissors]
com=random.randint(0,2)
if (user==0 and com==2) or (user==1 and com==0) or (user==2 and com==1):
  print("Congraulations you win")
  print(f"You Chose\n {draw[user]}\nComputer Chose\n {draw[com]}")
elif user==com:
  print("Game is a tie")
  print(f"You Chose\n {draw[user]}\nComputer Chose\n {draw[com]}")
elif user<=2:
  print("Sorry you Lose try next time ")
  print(f"You Chose\n {draw[user]}\nComputer Chose\n {draw[com]}")
else:
  print("You entered wrong input you Lose")

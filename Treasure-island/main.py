print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#Write your code below this line 
choice=input('You\'re at a crossroad. Where do you want to go? Type "left" or "right"\n').lower()
if choice=='left':
 choice=input('You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across.\n').lower()
 if choice=='wait':
  choice=input('You have arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?"\n')
  if choice=='yellow':
   print('You found the treasure! You Win!')
  elif choice=='red':
   print("You enter a room of beasts. Game Over")
  elif choice=='blue':   
   print('You get attacked by an angry trout. Game Over.')
  else:  
   print("It's a room full of fire. Game Over.")
 else:  
  print("A mysterious creature drag you inside water, Game over.")  
else:  
 print("You have fallen into a hole game over")

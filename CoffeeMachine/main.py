from data import MENU,resources
import os

profit=0
def check_resoure(order_ingredients):
  """Returns True when order can be made, False if any ingredients is insufficient."""
  check=1
  low=[]
  for item in order_ingredients:
    if order_ingredients[item] > resources[item]:
      low.append(item)
      check=0
  if check:
    return True
  else:
    print("Sorry there is not enough",end=" ")
    for item in low:
      print(item,end=" ,")
    return False         

def cal_money(cof):
  """Calculate if coin amount>= required amount for making coffee if yes the return change"""
  req_cost=MENU[cof]["cost"]
  print("Please insert coins.")
  total=float(input("how many quarters?:"))/4
  total+=float(input("how many dimes?"))/10
  total+=float(input("how many nickles?:"))/20
  total+=float(input("how many pennies?:"))/100
  if total>=req_cost:
    global profit
    profit+=req_cost
    print(f"Here is your {round(total-req_cost,2)} dollars in change")
    return True 
  else:
    print("Sorry that's not enough money. Money refunded.")
    return False  

def make_coffee(order_ingredients,coffee_name):
  """Deduct the required ingredients from the resources."""
  for item in order_ingredients:
    resources[item] -= order_ingredients[item]
  print(f"Here is your {coffee_name} ☕️. Enjoy!")

while True:
  value=input("\nWhat would you like? (espresso/latte/cappuccino):").lower()
  if value=='report':
    for item in resources:
      print(f"{item} : {resources[item]}")
    print(f"Money : {profit}")  
  elif value=='off':
    exit()  
  else:
    drink=MENU[value]
    if check_resoure(drink["ingredients"]):
     if cal_money(value):
       make_coffee(drink["ingredients"],value) 
  

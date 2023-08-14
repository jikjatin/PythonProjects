alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
import os
from art import logo
print(logo)

def caesar():
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  if shift>26:
    shift=shift%26
#   shift=0
# else:
#    shift=shift-((shift//26)*26)
  shift_letter=''
  if direction=="encode":
    for letter in text:
      if letter in alphabet:
        shift_letter+= alphabet[alphabet.index(letter)+shift+1-27] #using reverser value of letter by decreasing 27 to solve the list index out of range error and adding 1 cuz list index starts from 0
      else:
        shift_letter+=letter
  elif direction=="decode":
    for letter in text:
      if letter in alphabet:
        shift_letter+= alphabet[alphabet.index(letter)-shift]
      else:
        shift_letter+=letter  
  print(f"Your {direction}d text is {shift_letter}")
  cont=input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")   
  if cont=='yes':
    os.system('cls')
    caesar()

caesar()

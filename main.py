import random
from colorama import Fore, Back
chars = "qwertzuiopasdfghjklyxcvbnmQWERTZUIOPASDFGHJKLYXCVBNM"

while 1:
  username_len = int(input("How long should the combination be =  "))
  username_count = int(input("How many combinations should be generated = "))
  for x in range(0,username_count):
    username = ""
  for x in range(0,username_len):
    username_char = random.choice(chars)
    username = username + username_char
    print(Fore.GREEN + 'Username generated:' , username)
import emoji
import random
import os

from subprocess import call 
  
def clear(): 
    _ = call('clear' if os.name =='posix' else 'cls') 

coins = 100 

a = [emoji.emojize(":skull:"), emoji.emojize(":cherries:"), emoji.emojize(":bell:"), emoji.emojize(":lemon:"), emoji.emojize(":tangerine:"), emoji.emojize(":white_medium_star:")]
answer = raw_input("Do you want to start?\n")
clear()

while answer == "yes":
  while coins >= 0:
    if answer != "yes":
      break
    x1, x2, x3 = random.randint(0,5), random.randint(0,5), random.randint(0,5)

    print("+--------+")
    print("|        |")
    print(">"),
    print(a[x1]),
    print(a[x2]),
    print(a[x3]),
    print(" <")
    print("|        |")
    print("+--------+")
    print(" ")
    if a[x1] == a[x2]:
      coins = coins + 50
    if a[x2] == a[x3]:
      coins = coins + 50
    if a[x1] + a[x2] + a[x3] == a[x1] + a[x2] + a[x3]:
      coins = coins + 100
    if a[x1] + a[x2] + a[x3] == emoji.emojize(":bell:") + emoji.emojize(":bell:") + emoji.emojize(":bell:"):
      coins = coins + 500
    if a[x1] + a[x2] == emoji.emojize(":skull:") + emoji.emojize(":skull:"):
      coins = coins - 100
    if a[x2] + a[x3] ==  emoji.emojize(":skull:") + emoji.emojize(":skull:"):
      coins = coins - 100
    if a[x1] + a[x2] + a[x3] ==  emoji.emojize(":skull:") + emoji.emojize(":skull:") + emoji.emojize(":skull:"):
      coins = 0
    print(emoji.emojize(":money_bag:") + "  " + str(coins) + " " + emoji.emojize(":money_bag:"))
    coins = coins - 20
    answer = "no"
    print(" ")
    answer = raw_input("Do you want to start again?\n")
    clear()
print("You finished the game with "+emoji.emojize(":money_bag:")+ "  " +str(coins))
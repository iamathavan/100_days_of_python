print(r'''
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
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
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
print("You're at a cross road. Where do you want to go ?")
t=input("\t type \"left\" or \"right\"").lower()
if (t=="left"):
    print("you've came to the lake. there is a island in the middle of the lake.")
    t2=input("\t type \"wait\" to wait for boat or type \"swim\" to swim the lake.").lower()
    if t2=="wait":
        print("you arrived island unharmed.there is house with three doors.")
        t3=input("\t one red, one yello and one blue, which do you choose?").lower()
        if t3=="red":
            print("entered the room full of fire. game over")
        elif t3=="yellow":
            print("You found the treasure. game won.")
        elif t3=="blue":
            print("entered the room full of beast. game over.")
        else:
            print("game over.")
    else:
        print("Attacked by trout. Game Over.")
else:
    print("Fall into a hole. Game Over.")
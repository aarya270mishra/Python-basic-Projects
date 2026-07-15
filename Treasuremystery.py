print('''*******************************************************************************
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
|___________________|_| ;     #) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_ 
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_ 
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/
*******************************************************************************''')
print("""Welcome to Treasure Island.\n
Your mission is to find the treasure""")
print("You're at a cross road. Where do you want to go? \n Type Left or Right" )
user_input = input("left or right? :\n")
if user_input == "right" or None:
    print("""Fall into a hole.
           Game Over""")
else:
    right_choice = input("""You've come to a lake. There is an island in the middle of the lake.\n
  Type "wait" to wait for a boat. Type "swim" to swim across. :\n""")
    if  right_choice == "swim":
        print("""Bitten by the Crocodile in the lakes
              Game Over !""")
    else:
        wait_choice = input("""You Have Reached to the island safely
              There are three Doors (red , yellow , blue) where you will go :\n""").lower()
        if wait_choice == "red":
            print("""There was fire in the room 
                  Game Over !""")
        elif wait_choice == "blue":
            print("""The room was full of insects!
                  Game Over !""") 
        else:
            print("You Won !!!!!...Founded Treasure Successfully")       


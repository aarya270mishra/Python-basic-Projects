import random 

number=random.randrange(1,50)

print("Lets play guessing the number challaenge")

print("""=========================THE RULES===================================
      choose any number btw 1-50 
      if thats number closer to the answer then you are hot and if 
      thats far you are cold """)

while True:
    guess=int(input("Enter your number:"))
    if number ==guess:
        print(f"Your guessed it right ! The number was {number}")
        print("==============================================================")
        break 
    else:
        if abs(number-guess) <=5:
            print("You are Hot")
        else:
            print("You are Cold !")



    

    








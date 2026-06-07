import random 
#Specifying the opponents choices 
opponent = ["rock" , "paper" , "scissor"]

random_opponent = random.choice(opponent)  #.choice() allows random choice among strings

print("Lets Play Rock Paper Scissors !")

while True:
    user_choice=input("Enter your choice (rock/paper/scissor):").lower()

    print(f" Computer choosed : {random_opponent}")

    if user_choice == "rock" and random_opponent == "paper":
        print("HaHaHA.. you lost !")
        

    elif user_choice == "rock" and random_opponent == "scissor":
        print("You Won..")
        

    elif user_choice == "paper" and random_opponent == "rock":
         print("You Won..")
         
    
    elif user_choice == "paper" and random_opponent == "scissor":
        print("HaHaHA.. you lost !")
        

    elif user_choice == "scissor" and random_opponent == "rock":
        print("HaHaHA.. you lost !")
        

    elif user_choice == "scissor" and random_opponent == "paper":
        print("You Won ! :)")

    elif user_choice ==random_opponent:
        print("Its a tie !")    
        
    else:
        print("Invalid choice")

    again =print("Want to play again (y/n)")
    if again !='y':
        break  









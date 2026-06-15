import time 

print("Hiii, Welcome")
ans = str(input(r"Do You want to play a quiz game (yes/no): "))

if ans!="yes":
    quit(0)
else:
    print("Hurayy!..Lets play") 

print('=================================================================')
time.sleep(3)

score=0
que1 = input("The  brain of any computer system is: ").upper()
if que1 =="CPU":
    print("Correct !")
    score+=1
    
else:
    print("Wrong anser")  
print(f"Your score {score}")    


time.sleep(2)
ques2 = input("Which of the following language does the computer understand? :").lower()
if ques2 == "binary":
    print("Corect !")
    score+=1

else:
    print("Wrong answer")    
print(f"Your score {score}") 

time.sleep(2)
ques3 = input("Which device is used to input data into a computer?").lower()
if ques3 == "keyboard":
    print("Correct !")
    score+=1
else:
    print("Wrong answer")
print(f"Your score {score}") 


time.sleep(2)
ques4 = input("What is the full form of RAM? :").lower()
if ques4 == "random access memory":
    print("Correct !")
    score+=1
else:
    print("Wrong answer")  
print(f"Your score {score}")    

print("Now lets move to the last question")



time.sleep(2)
ques5 = input("What does GUI stand for? :").lower()
if ques5 == "graphical user interface":
    print("Correct !")
    score+=1
    time.sleep(2)
else:
    print("Wrong answer")
    time.sleep(2)
print(f"Your Final score is {score} out of 5")     

print("WITH THAT THE QUIZ ENDS") 
print("==================================================================")       



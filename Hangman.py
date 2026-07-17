import time
import random 
from Hangman_words import words
from Hangman_art import hangmanpics


print('*' *50)
logo = ('''
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/                       ''')


print(logo)
print('*' *50)
time.sleep(1)



#   Instructions for the User
print("""
----------------------HANGMAN INSTRUCTIONS----------------------------

Instructions:
• Guess the hidden word one letter at a time.
• Correct guesses reveal the letters.
• Wrong guesses cost one life.
• You have 5 lives.
• Guess the word before you run out of lives.
""")


time.sleep(3)
print("LETS START \n")


# Generate a random Word from the list 
random_word = random.choice(words)


# Create a "placeholder with the same number of blanks as choosen words"
placeholder = ""
word_length = len(random_word)
for position in range(word_length):
    placeholder += "_"
print(placeholder)   


correct_letters = []
game_over = False

# Keep Track of User Lives 
lives = 5




# Loop for Repetition of the input from user 
while not game_over:





    print(f"****************** {lives}/ 5 lives left *********************")



# 1. Take user input for the alphabet 
    user_guess = input("Guess the Letter :").lower()
    print(user_guess)

   # if the user has entered a letter they've already guessed , print already guessed 
    if user_guess  in correct_letters:
        print(f"You've already Guessed the letter {user_guess}")
        continue




# 2 .Create a display that will print the right positioned alphabet in the right place and print '_' in the rest

    display = ""
    for letter in random_word:
        if letter == user_guess:
            display +=letter
            correct_letters.append(user_guess)
        elif letter in correct_letters:
            display += letter
        else:
            
            display += "_"
    print(display)


    


    # Deduct lives and display hangman position 
    if user_guess not in random_word:
        lives -=1
        print(f"You Guessed letter {user_guess} that's not in Word , So you loose a life")
        print("Lives Remaining ",lives)
        if lives == 0:
            game_over = True
            print(f"*******************IT WAS {random_word} You Lose **********************")

    
    print(hangmanpics[lives])


    if  "_" not in display:
        time.sleep(1)
        game_over = True
        print("*********************** You Win ************************")
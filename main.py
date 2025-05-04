#HangMan game: 
import random
from hangman_words import word_list
from hangman_art import stages, logo 
import os

def clear():
    os.system("cls" if os.name == "nt" else "clear")

choosen_word = random.choice(word_list)
word_length = len(choosen_word)
display = ["_"] * word_length
mistake_letter = []
lives = 6

print(choosen_word)
end_of_game = False
while not end_of_game:
    clear()
    print(logo)
    print(stages[lives])
    print(f"Lives left: {lives}")
    word = ' '.join(display)
    print(word)
    print(f"Wrong guesses: {','.join(mistake_letter)}")
    choice = input("Enter a letter you choose: ").lower()
    
     
    if choice in mistake_letter or choice in display:
        print(f"{choice} is already guessed.")
        

    elif choice in choosen_word:   
        for index, letter in enumerate(choosen_word):
            if letter == choice:
                display[index] = choice
        print(f"Nice!, {choice} is in the word.")            
    else:
        
        mistake_letter.append(choice)
        lives -= 1
        print(f"Oops!, {choice} is not in word. You lose a life.")
    #print(word)

    if lives == 0:
        end_of_game = True
        clear()
        print(logo)
        print("You lose.")
        print(f"The correct word was {choosen_word}")

    elif "_" not in display:
        end_of_game = True
        clear()
        print(logo)
        print(stages[lives])
        print("You win")
        print("The word was:", choosen_word)

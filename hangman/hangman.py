from words import words
import random
import string

def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word.upper()

def hangman():
    word = get_valid_word(words)
    word_letters = set(word) # letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set() # what the user has guessed 

    lives = 6

    # getting user input
    while len(word_letters) > 0 and lives > 0:
        #letters used
        print("You have used these letters: ", ' '.join(used_letters))
        print(f"You have {lives} lives left")

        # what current word is
        word_list = [letter if letter in used_letters else "_" for letter in word]
        print("Current word is ", ' '.join(word_list))

        user_letter = input("Guess a letter: ").upper()
        if user_letter in (alphabet - used_letters):
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            
            else:
                lives = lives - 1
                print("Letter is not in the word.")

        elif user_letter in used_letters:
            print("You have already used that character.")

        else:
            print("Invalid character.")

    if lives == 0:
        print(f"You died. The word is {word}")
    else:
        print(f"You won! The word is {word}")

hangman()
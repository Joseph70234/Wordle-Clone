from colorama import Fore, init
import nltk
from nltk.corpus import words
import random

# list of 5-letter words
#nltk.download('words')
five_letter_words = [word for word in words.words() if len(word) == 5 and word.islower()]
word = random.choice(five_letter_words)

# initialize colorama
init(autoreset=True)

# initialize answer grid
giga_grid = ''

# gameplayloop
i = 1
grid_num = 5
while i <= 5:

    print(giga_grid + '_ _ _ _ _ \n'*grid_num)

    print(word)
    user_input = input("Enter exactly 5 letters: ")
        
    # Check if the input is exactly 5 characters and only contains letters
    if user_input.isalpha() and len(user_input) == 5 and user_input in five_letter_words:
        build_guess = ''

        # loop through letters
        for count in range(5):
                if user_input[count] == word[count]:
                    build_guess += Fore.GREEN + user_input[count] + ' '
                
                elif user_input[count] in word:
                    build_guess += Fore.YELLOW + user_input[count] + ' '

                else:
                    build_guess += Fore.LIGHTBLACK_EX + user_input[count] + ' '

        i += 1
        grid_num -= 1

        giga_grid += build_guess + '\n'

        if user_input == word:
            print(giga_grid + '_ _ _ _ _ \n'*grid_num)
            break

    else:
        print("Invalid input.")

if i == 2:
    print('Cheater?')
elif i == 3:
    print('Impressive!')
elif i == 4:
    print('Well done!')
elif i == 5:
    print('Great!')
elif i == 6:
    print('Phew!')
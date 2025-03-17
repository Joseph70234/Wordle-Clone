from colorama import Fore, init
import random
import requests
from wordfreq import top_n_list

# list of wordle words
wordle_url = "https://raw.githubusercontent.com/tabatkins/wordle-list/main/words"
words = requests.get(wordle_url).text.split("\n")

common_words = [word for word in top_n_list("en", 50000) if len(word) == 5]

final_list = []
for word in common_words:
    if word in words:
        final_list.append(word)

word = random.choice(final_list)

# initialize colorama
init(autoreset=True)

# initialize answer grid
giga_grid = ''

# gameplay loop
i = 1   # attempt number
grid_num = 5    # number of blank lines in grid

win = False
while win == False:

    # print current grid
    print(giga_grid + '_ _ _ _ _ \n'*grid_num)

    # if user has lost
    if i == 6:
        break

    # gather guess
    user_input = input("Enter exactly 5 letters: ")
        
    # check if input is 5 letters
    if user_input.isalpha() and len(user_input) == 5 and user_input in words:
        build_guess = ''

        # check guess
        for count in range(5):
                
                # if letter in correct position
                if user_input[count] == word[count]:
                    build_guess += Fore.GREEN + user_input[count] + ' '
                
                # if letter in word, but incorrect position
                elif user_input[count] in word:
                    build_guess += Fore.YELLOW + user_input[count] + ' '

                # if letter not in word
                else:
                    build_guess += Fore.LIGHTBLACK_EX + user_input[count] + ' '

        # setup next try and grid
        i += 1
        grid_num -= 1
        giga_grid += build_guess + '\n'

        # if the user has won
        if user_input == word:
            win = True
            print(giga_grid + '_ _ _ _ _ \n'*grid_num)
            break

    else:
        print("Invalid input.")

# winning dialogue
if grid_num == 4:
    print('Cheater?')
elif grid_num == 3:
    print('Impressive!')
elif grid_num == 2:
    print('Well done!')
elif grid_num == 1:
    print('Great!')
elif grid_num == 0 and win == True:
    print('Phew!')

if win == False:
    print('You suck')
    print(f'The word was {word}.')
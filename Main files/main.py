import random

rand = random
print("""
=-=-=-=-=-=-=-=-=-=-=
Hi there you may know the game hangman right? if you don't its basically a game where you guess the letters 
of a word chosen by the 'host' and for each one you get wrong they slowly draw a man getting hanged on a board  or paper
but here we just have a life system you get 11 so make em count now that you get the jist of it lets get started
=-=-=-=-=-=-=-=-=-=-=
""")

selection = input("""
Healthy food [H]
Junk Food [J]
Drinks [D]
-=-=-=-=-=-=-=-=-=-=-=-
Choose between these categories:
=-=-=-=-=-=-=-=-=-=-=-=
""")


def junkfoodcat():
    word_list = ['burger', 'fries', 'cheeseburger', 'taco', 'slushy', 'candy corn']
    word = rand.choice(word_list)
    letters = []
    solved = False
    lives = 11

    while not solved:
        user_char = input("please enter one letter: ").lower()
        char = len(str(user_char))

        if char < 1:
            print('Please enter a letter: ')
        elif char > 1:
            print(f'please enter only one letter ')
        elif user_char not in word:
            print('oops wrong letter try again')

        if user_char not in letters:
            letters.append(user_char)

        output = ''
        for letter in word:
            if letter in letters:
                output += letter
            else:
                output += "_"
        print(output)

        if output == word:
            print('You won!')
            break
        elif user_char not in word:
            lives -= 1
            print(f"You have {lives} lives left")
            if lives == 0:
                print("Sorry you lost try again next time")
                break


def healthyfoodcat():
    word_list = ['salad', 'tomato', 'ginger', 'apple', 'orange', 'vegetables']
    word = rand.choice(word_list)
    letters = []
    solved = False
    lives = 11

    while not solved:
        user_char = input("please enter one letter: ")
        char = len(str(user_char))

        if char < 1:
            print('Please enter a letter: ')
        elif char > 1:
            print(f'please enter only one letter ')
        elif user_char not in word:
            print('oops wrong letter try again')

        if user_char not in letters:
            letters.append(user_char)

        output = ''
        for letter in word:
            if letter in letters:
                output += letter
            else:
                output += "_"
        print(output)

        if output == word:
            print('You won!')
            break
        elif user_char not in word:
            lives -= 1
            print(f"You have {lives} lives left")
            if lives == 0:
                print("Sorry you lost try again next time")
                break


def drinkscat():
    word_list = ['water', 'coke', 'fanta', 'sprite', 'juice', 'smoothie']
    word = rand.choice(word_list)
    letters = []
    solved = False
    lives = 11

    while not solved:
        user_char = input("please enter one letter: ")
        char = len(str(user_char))

        if char < 1:
            print('Please enter a letter: ')
        elif char > 1:
            print(f'please enter only one letter ')
        elif user_char not in word:
            print('oops wrong letter try again')

        if user_char not in letters:
            letters.append(user_char)

        output = ''
        for letter in word:
            if letter in letters:
                output += letter
            else:
                output += "_"
        print(output)

        if output == word:
            print('You won!')
            break
        elif user_char not in word:
            lives -= 1
            print(f"You have {lives} lives left")
            if lives == 0:
                print("Sorry you lost try again next time")
                break


if selection.upper() == 'J':
    junkfoodcat()
elif selection.upper() == 'H':
    healthyfoodcat()
elif selection.upper() == 'D':
    drinkscat()

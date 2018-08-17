import random

def greeting():
    print('-----------------------------')
    print(" GUESS THE NUMBER I CHOSE...")
    print('-----------------------------')
    print('')
    name = input("Welcome player, your name: ")
    return name

def ask_choice():
    choice = input("\nChoose a number between 0 and 100:")
    return int(choice)

def eval_choice(name, choice, number):
    result = 0
    if choice > number + 10:
        print ('Sorry {1}, your choice {0} was TOO HIGH!'.format(choice, name))
    elif choice < number - 10:
        print ('Sorry {1}, your choice {0} was TOO LOW!'.format(choice, name))
    elif choice > number:
        print ('Sorry {1}, close, but your choice {0} was a little high'.format(choice, name))
    elif choice < number:
        print ('Sorry {1}, close, but your choice {0} was a little low'.format(choice, name))
    else:
        print("\nCongratulations {1}, {0} was my choice!".format(choice,name))
        result = 1

    return result

if __name__ == "__main__":
    guess = random.randint(0,100)
    name = greeting()
    choice = ask_choice()
    while not eval_choice(name, choice, guess):
        choice = ask_choice()

    print("\n GAME ENDED, C YA!")

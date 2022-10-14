import random

def get_computer_choice():
    options = ['Rock', 'Paper', 'Scissors']
    computer_choice = random.choice(options)
    print(computer_choice)
    return computer_choice


def get_user_choice():
    user_choice = input('Enter your choice: ')
    return user_choice

get_computer_choice()
get_user_choice()
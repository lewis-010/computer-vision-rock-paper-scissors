import random

def get_computer_choice():
    options = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(options)
    print(computer_choice)
    return computer_choice


def get_user_choice():
    user_choice = input('Enter your choice: ')
    return user_choice

def get_winner(computer_choice, user_choice):
    computer_choice = get_computer_choice()
    user_choice = get_user_choice()
    if (computer_choice=="rock" and user_choice=="scissors") or (computer_choice=="paper" and user_choice=="rock") or (computer_choice=="scissors" and user_choice=="paper"):
        print("Computer wins!")
    elif (computer_choice=="rock" and user_choice=="paper") or (computer_choice=="paper" and user_choice=="scissors") or (computer_choice=="scissors" and user_choice=="rock"):
        print("You win!")
    else:
        print("Draw!")

def play():
    get_computer_choice()
    get_user_choice()
    get_winner(computer_choice=get_computer_choice, user_choice=get_user_choice)

play()

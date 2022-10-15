import random

# gets computer's choice of rock, paper or scissors
def get_computer_choice():
    options = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(options)
    # print(computer_choice)
    return computer_choice

# gets user's choice of rock, paper or scissors
def get_user_choice():
    user_choice = input('Enter your choice: ')
    return user_choice

# determines winner based on value of computer_choice and user_choice
def get_winner(computer_choice, user_choice):
    if (computer_choice=="rock" and user_choice=="scissors") or (computer_choice=="paper" and user_choice=="rock") or (computer_choice=="scissors" and user_choice=="paper"):
        print("Computer wins!")
    elif (computer_choice=="rock" and user_choice=="paper") or (computer_choice=="paper" and user_choice=="scissors") or (computer_choice=="scissors" and user_choice=="rock"):
        print("You win!")
    else:
        print("Draw!")

# calls all three previous functions to play the game
def play():
    get_winner(computer_choice=get_computer_choice(), user_choice=get_user_choice())

play()

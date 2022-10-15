import random

# gets computer's choice of rock, paper or scissors
def get_computer_choice():
    options = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(options)
    # print(computer_choice)
    return computer_choice

# gets user's choice of rock, paper or scissors
def get_user_choice():
    while True:
        choices = ['rock', 'paper', 'scissors']
        user_choice = input('Enter your choice: ').lower()
        if user_choice in choices:
            break
        else:
            print("That is not a valid input. Please choose from rock, paper or scissors.")
    return user_choice

# determines winner based on value of computer_choice and user_choice
def get_winner(computer_choice, user_choice):
    if (computer_choice=="rock" and user_choice=="scissors") or (computer_choice=="paper" and user_choice=="rock") or (computer_choice=="scissors" and user_choice=="paper"):
        print("Computer wins!")
    elif (computer_choice=="rock" and user_choice=="paper") or (computer_choice=="paper" and user_choice=="scissors") or (computer_choice=="scissors" and user_choice=="rock"):
        print("You win!")
    else:
        print("Draw!")

# calls all three previous functions to play the game and give option to play the game again
def play():
    computer_choice = get_computer_choice()
    user_choice = get_user_choice()
    get_winner(computer_choice, user_choice)
    while True:
        play_again = input("Would you like to play again? (y/n): ")
        if play_again.lower() == "y":
            play()
        else:
            print("Game over.")
        break             
    
play()

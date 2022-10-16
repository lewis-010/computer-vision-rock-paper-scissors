import random

def get_computer_choice():
    '''Returns computer's random choice of rock, paper or scissors from the options list.'''
    options = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(options)
    # print(computer_choice)
    return computer_choice

def get_user_choice():
    '''Returns user's choice of rock, paper or scissors based on user input.
        
        Validiity of user input is also checked.'''
    while True:
        choices = ['rock', 'paper', 'scissors']
        user_choice = input('Enter your choice: ').lower()
        if user_choice in choices:
            break
        else:
            print("That is not a valid input. Please choose from rock, paper or scissors.")
    return user_choice

def get_winner(computer_choice, user_choice):
    '''Determines the winner of the ganme (computer or user)
        
        Parameters:
            computer_choice (str): computer's choice of rock, paper or scissors.
            user_choice (str): user's choice of rock, paper or scissors.
    '''
    if (computer_choice=="rock" and user_choice=="scissors") or (computer_choice=="paper" and user_choice=="rock") or (computer_choice=="scissors" and user_choice=="paper"):
        print("Computer wins!")
    elif (computer_choice=="rock" and user_choice=="paper") or (computer_choice=="paper" and user_choice=="scissors") or (computer_choice=="scissors" and user_choice=="rock"):
        print("You win!")
    else:
        print("Draw!")

def play():
    '''Calls the three previous functinons to run the game.
    
        Option to play the game again provided, based on user input.'''
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
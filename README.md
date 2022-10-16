# The Computer Vision Project
Rock, paper, scissors is a classic game played by two or more people and relies on the visual input of, usually, a player's hand. This project focuses on the creation of a computer vision system, or model, to detect whether the user is showing rock, paper, scissors or nothing to the camera, and to then use a python script to play the game.
<br/><br/>

## Milestone 1
- The first task was to create a machine learning model using the online service [Teachable Machine](https://teachablemachine.withgoogle.com/).
- Teaching Machine took visual samples of a player holding up rock, paper, scissors and nothing to create the respective four classes in the model.
- A sample size of 200 images for each class was used.
<br/><br/>

## Milestone 2
- Virtual envrironment setup through the [Conda](https://anaconda.org/anaconda/conda) environment management system.
- Libraries installed into virtual environment with pip:
    - OpenCV-python
    - Tensorflow
    - Ipykernel
<br/><br/>
- If users wish to install all dependencies for this project, use *pip install requirements.txt*.
- Requires prior installation of pip in the same environment.
<br/><br/>

## Milestone 3
- *manual_rps.py* file created within the above virtual environment to play the game without the need for a computer vision system model or camera. 
- Users can simply run the script, input their choice of rock, paper or scissors into the terminal and find out if they have won, lost or drawn.
- The option to play again without re-running the the script is also provided after the result of the game has been outputted.
```python
import random

def get_computer_choice():
    '''Returns computer's random choice of rock, paper or scissors from the options list.'''
    options = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(options)
    # print(computer_choice)
    return computer_choice

def get_user_choice():
    '''Returns user's choice of rock, paper or scissors based on user input.
        
        Validiity of user input is also checked.
    '''
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
    
        Option to play the game again provided, based on user input.
    '''
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
```
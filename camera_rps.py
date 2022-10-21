import cv2
import random
from keras.models import load_model
import numpy as np
import time

model = load_model('keras_model.h5')
cap = cv2.VideoCapture(0)
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

class Rps:
    def __init__(self):
        '''
        Attributes:
        ----------
        computer_wins: 
            The number of wins the computer has.
        user_wins:
            The number of wins the user has.
        options: list
            The options from which the computer vision model assigns to the user based on their visual gesture. 
        '''
        self.computer_wins = 0
        self.user_wins = 0
        self.options = ['rock', 'paper', 'scissors', 'nothing']
   
    def get_computer_choice(self):
        '''
        Randomly selects the computer's choice for each game from computer_options list.

        Returns:
            computer_choice: rock, paper or scissors.
        '''
        computer_options = ['rock', 'paper', 'scissors']
        computer_choice = random.choice(computer_options)
        return computer_choice

    def get_user_choice(self):
        '''
        Uses the computer vision model (keras_model.h5) to determine the user's choice. 
        Runs inside the while loop for 1 second and outputs text to camera feed describing user's choice (cv2.putText)

        Returns:
            user_choice: rock, paper, scissors or nothing.
        '''
        t_end = time.time()+1
        while t_end > time.time(): 
            ret, frame = cap.read()
            font = cv2.FONT_HERSHEY_SIMPLEX
            resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
            image_np = np.array(resized_frame)
            normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # normalize the image
            data[0] = normalized_image
            prediction = model.predict(data)
            user_choice = np.argmax(prediction)
            cv2.putText(frame, f"User Choice {self.options[user_choice]} ", (50, 50), font, 1, (0, 255, 255), 2, cv2.LINE_4)
            cv2.imshow('frame', frame)
            # Press q to close the window
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        return self.options[user_choice].lower()

    def get_winner(self):
        '''
        Runs the above two functions to get user/computer choice and determines winner based on if functions.

        Output:
            print statement describing the winner.
            adds 1 to the relecant class attribute (user_wins or computer_wins)
        '''
        computer_choice = self.get_computer_choice()
        user_choice = self.get_user_choice()
        print("Computer choice:", computer_choice)
        print("User choice:", user_choice)

        if (computer_choice=="rock" and user_choice=="scissors") or (computer_choice=="paper" and user_choice=="rock") or (computer_choice=="scissors" and user_choice=="paper"):
            print("Computer wins!")
            self.computer_wins+=1
        elif (computer_choice=="rock" and user_choice=="paper") or (computer_choice=="paper" and user_choice=="scissors") or (computer_choice=="scissors" and user_choice=="rock"):
            print("You win!")
            self.user_wins+=1
        else:
            print("Draw!")           

    def countdown(self):
        '''
        Runs a countdown in the form of a classic rock, paper, scissors game. 
        Allows time for user to make a choice.

        Output:
            print statements: ROCK, PAPER, SCISSORS, SHOOT
        '''
        print("The game will start soon, make your choice now!")
        time.sleep(3)
        print("ROCK")
        time.sleep(1)
        print("PAPER")
        time.sleep(1)
        print("SCISSORS")
        time.sleep(1)
        print("SHOOT")
        time.sleep(1)

def play_game():
    '''
    Instance of the class Rps created (play). Runs the above functions to play the game (limit of 3 wins set before game ends).

    Output:
        print statememt for winner of each game.
        print statememt for winner of the overall game once 3 have been won by user or computer.
    '''
    print("Let's play rock, paper, scissors. First to three wins!")
    time.sleep(2)
    play = Rps()
    while play.user_wins < 3 or play.computer_wins < 3:
        play.countdown()
        play.get_winner()
        print(f"Computer wins: {play.computer_wins}")
        print(f"User wins: {play.user_wins}")

        if play.user_wins == 3:
            print("Nice! You have won 3 games.")
            break
        elif play.computer_wins == 3:
            print("Unlucky! The computer has won 3 games.")
            break

    # After the loop release the cap object
    cap.release()
    # Destroy all the windows
    cv2.destroyAllWindows()

play_game()
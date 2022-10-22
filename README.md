# The Computer Vision Project
Rock, paper, scissors is a classic game played by two or more people and relies on the visual input of, usually, a player's hand. This project focused on providing a way for users to play a game against the computer using physical gestures. In order to do this, a computer vision model, that can recognise the various hand gestures, was combined with a python script that runs the game and keeps track of the scores. 
<br/><br/>

## Milestone 1
- The first task was to create a machine learning model that recognises a user's choice of rock, paper or scissors, using the online service [Teachable Machine](https://teachablemachine.withgoogle.com/). 
- Teaching Machine took visual samples of a player holding up rock, paper, scissors and nothing to create the respective four classes in the model which was then exported (*keras_model.h5*).
- A sample size of 200 images for each class was used., although increasing this value would improve the accuracy of the model.
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
<br/><br/>
## Milestone 4
- *camera_rps.py* file integrates the computer vision model, created in milestone 1, that can recognise a players choice or rock, paper or scissors through the webcam, with a python script similar to that in milestone 3.
- The main differences are as follows:
    - class created to ensure better readability
    - get_user_choice function replaced with the model_check.py code that combines the computer vision model with the python script
    - score tracking code added to get_winner function (limit of 3 wins for user or computer before script ends)
    - countdown function added in the same format of a classic rock, paper, scissors game (ROCK, PAPER, SCISSORS, SHOOT, *get_user_choice runs*)
    - text added to camera display that describes the user's choice
<br/><br/>
- note - doc strings added in *camera_rps.py* file.
```Python
import cv2
import random
from keras.models import load_model
import numpy as np
import time

# load computer vision model
model = load_model('keras_model.h5')
cap = cv2.VideoCapture(0)
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

class Rps:
    # initialize class and set user/computer win attrbutes to 0
    def __init__(self):
        self.computer_wins = 0
        self.user_wins = 0
        self.options = ['rock', 'paper', 'scissors', 'nothing']

    # select random computer choice from list of options
    def get_computer_choice(self):
        computer_options = ['rock', 'paper', 'scissors']
        computer_choice = random.choice(computer_options)
        return computer_choice

    # select user choice using webcam/computer vision model (model runtime limited to 1 second)
    def get_user_choice(self):
        t_end = time.time()+1
        while t_end > time.time(): 
            ret, frame = cap.read()
            font = cv2.FONT_HERSHEY_SIMPLEX
            resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
            image_np = np.array(resized_frame)
            # normalize the image
            normalized_image = (image_np.astype(np.float32) / 127.0) - 1 
            data[0] = normalized_image
            prediction = model.predict(data)
            user_choice = np.argmax(prediction)

            # add user choice as text to camera feed on the screen
            cv2.putText(frame, f"User Choice {self.options[user_choice]} ", (50, 50), font, 1, (0, 255, 255), 2, cv2.LINE_4)
            cv2.imshow('frame', frame)
            # Press q to close the window
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        return self.options[user_choice].lower()

    # determine winner based on if statements and add 1 win to the relevant attribute (user_wins or computer_wins)
    def get_winner(self):
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

    # provide user with time to make a decision in the form of a classic rock, paper, scissors countdown
    def countdown(self):
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

# create instance of class Rps (play) inside play_game function and set limit of wins to 3 before code ends
def play_game():
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

    # after the loop release the cap object
    cap.release()
    # destroy all the windows
    cv2.destroyAllWindows()

play_game()
```
import random
import cv2
from keras.models import load_model
import numpy as np

model = load_model('keras_model.h5')
cap = cv2.VideoCapture(0)
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

class RPS:
    def __init__(self):
        self.computer_wins = 0
        self.user_wins = 0
        self.options = ['rock', 'paoer', 'scissors', 'nothing']
   
    def get_computer_choice():
        options = ['rock', 'paper', 'scissors']
        computer_choice = random.choice(options)
        # print(computer_choice)
        return computer_choice

    def get_user_choice():
        while True: 
            ret, frame = cap.read()
            resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
            image_np = np.array(resized_frame)
            normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
            data[0] = normalized_image
            prediction = model.predict(data)
            user_choice = np.argmax(prediction)
            cv2.imshow('frame', frame)
            # Press q to close the window
            print(prediction)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        return user_choice.lower()
                
        # After the loop release the cap object
        cap.release()
        # Destroy all the windows
        cv2.destroyAllWindows()

    def get_prediction(computer_choice, user_choice):
        if (computer_choice=="rock" and user_choice=="scissors") or (computer_choice=="paper" and user_choice=="rock") or (computer_choice=="scissors" and user_choice=="paper"):
            print("Computer wins!")
        elif (computer_choice=="rock" and user_choice=="paper") or (computer_choice=="paper" and user_choice=="scissors") or (computer_choice=="scissors" and user_choice=="rock"):
            print("You win!")
        else:
            print("Draw!")

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

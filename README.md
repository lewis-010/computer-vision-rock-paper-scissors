# The Computer Vision Project
Rock, paper, scissors is a classic game played by two or more people and relies on the visual input of, usually, a player's hand. This project focuses on the creation of a computer vision system, or model, to detect whether the user is showing rock, paper, scissors or nothing to the camera, and to then use a python script to play the game.
<br/><br/>

## Milestone 1
- The first task was to create a machine learning model using the online service [Teachable Machine](https://teachablemachine.withgoogle.com/).
- Teaching Machine took visual samples of a player holding up rock, paper, scissors and nothing to create the respective four classes in the model.
- A sample size of 200 images for each class was used.
<br/><br/>

## Milestone 2
- Install necessary libraries:
    - OpenCV-python
    - Tensorflow
    - Ipykernel
<br/><br/>
- If users wish to install all dependencies for this project, use *pip install requirements.txt*.
- Requires prior installation of pip in the same environment.
<br/><br/>

## Milestone 3
- *manual_rps.py* file created to play the game without the need for a computer vision system model or camera. 
- Users can simply run the script, input their choice of rock, paper or scissors into the terminal and find out if they wo, lost or drew.
- The option to play again without re-running the the script is also provided after the result of the game has been outputted.
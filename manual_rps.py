import random

def get_computer_choice():
    with open("labels.txt") as file:
        allText = file.read()
        words = list(map(str, allText.split()))
        computer_choice = random.choice(words)
    return computer_choice


def get_user_choice():
    user_choice = input("Enter your choice: ")
    return user_choice


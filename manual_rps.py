import random

def get_computer_choice():
    with open("labels.txt") as file:
        allText = file.read()
        words = list(map(str, allText.split()))
        computer_choice = random.choice(words)
        print(computer_choice)
    return computer_choice


def get_user_choice():
    user_choice = input("Enter your choice: ")
    return user_choice

get_computer_choice()
get_user_choice()
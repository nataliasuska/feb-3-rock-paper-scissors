import os
import random
from dotenv import load_dotenv

load_dotenv()
human_name = os.getenv("human_name", default="human")

print("-------------------")
print(f"Welcome {human_name} to a Rock-Paper-Scissors game with Nat!")
print("-------------------")

while True:
    human_choice = input("Please select either rock, paper, or scissors:")
    print(f"You chose: {human_choice}")
    human_choice = human_choice.lower()
    choices = ['rock', 'paper', 'scissors']    
    if human_choice not in choices:
        print("Oops, please select from rock, paper, or scissors and try again.")
        continue

    natbot_choice = random.choice(choices)
    print(f"Nat chose: {natbot_choice}")
    print("-------------------")

    if natbot_choice == "scissors" and human_choice == "rock":
        print("Congrats! You Won!")
    elif natbot_choice == "rock" and human_choice == "paper":
        print("Congrats! You Won!")
    elif natbot_choice == "paper" and human_choice == "scissors":
        print("Congrats! You Won!")
    elif natbot_choice == human_choice:
        print("It's a tie!")
    else:
        print("Oh, Nat won. Please don't cry...")

    while True:
        answer = str(input('Do you want to play again? Say yes or no:'))
        if answer in ('yes','no'):
            break
        print("Oops, please write either 'yes' or 'no':")
    if answer == 'yes':
        continue
    else:
        print("-------------------")
        print("Thanks for playing, I hope you had fun here. Please play again soon!")
        print("-------------------")
        break

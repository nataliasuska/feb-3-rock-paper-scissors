import random

print("-------------------")
print("Welcome 'Player One' to a Rock-Paper-Scissors game with Nat!")
print("-------------------")

human_choice = input("Please select either rock, paper, or scissors")
print(f"You chose: {human_choice}")

choices = ['rock', 'paper', 'scissors']
natbot_choice = random.choice(choices)
print(f"Nat chose: {natbot_choice}")

print("-------------------")


print("Oh, the computer won. It's ok.")
print("-------------------")
print("Thanks for playing. Please play again!")

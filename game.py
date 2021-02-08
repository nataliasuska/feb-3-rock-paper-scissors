import random

print("-------------------")
print("Welcome 'Player One' to a Rock-Paper-Scissors game with Nat!")
print("-------------------")

human_choice = input("Please select either rock, paper, or scissors:")
print(f"You chose: {human_choice}")

choices = ['rock', 'paper', 'scissors']
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

print("-------------------")
print("Thanks for playing, I hope you had fun here. Please play again soon!")
print("-------------------")

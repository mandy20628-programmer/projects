# rock paper scssiors
from random import random


def game():
    user_choice = input("Enter your choice (rock, paper, scissors): ").lower()
    import random
    computer_choice= random.choice(["rock","paper","scissors"])
    print(f"Computer chose: {computer_choice}")
    if user_choice==computer_choice:
        print("It's a tie!")
    else:
        if (user_choice=="rock" and computer_choice=="scissors") or (user_choice=="paper" and computer_choice=="rock") or (user_choice=="scissors" and computer_choice=="paper"):
            print("You win!")
        else:
            print("Computer wins!")
    a=input("want to play again? (yes/no): ")
    print(a)
    if a =="yes":
        game()
game()

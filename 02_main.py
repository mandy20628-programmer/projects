# rock paper scissors game
a=input("Enter your choice (rock, paper, scissors): ")
dict = {"rock": 0, "paper": 1, "scissors": 2}
a_values=dict[a]
import random
b = random.choice(["rock", "paper", "scissors"])
b_values=dict[b]
if a_values==b_values:
    print(f"Both players selected {a}. It's a tie!")
else:
    if (a_values - b_values) % 3 == 1:
        print(f"""Computer selected {b}.
{a} beats {b}. You win!""")
    else:
        print(f"""Computer selected {b}.
{b} beats {a}. You lose!""")
        
        user_input = input("Do you want to play again? (yes/no): ")
        if user_input.lower() == "yes":
            exec(open("02_main.py").read()) 
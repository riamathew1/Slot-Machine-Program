# Pokies
# Ria 25/2/26

import random

REELS = [
    ["😊", "🍔", "🚀"],
    ["🍔", "🤕", "🚀"],
    ["😊", "🍔", "🤕"]
]

# Greet the user to the program
print("Welcome to the slot machine!\n")

# Display the preview of the symbols
for reel in REELS:
    print(" | ".join(reel))

# Explain rules of program to user
print("\nYou will come across a face that shows 9 symbols.")
print("Get three matching symbols in the middle row and you win $500!")
print("If none of the symbols match you lose $200. Good luck!\n")

user_play = "y"
balance = 100000

while balance >= 200:
    user_play = input(f"You currently have ${balance}. Spin for $500? y/n  ").lower().strip()

    # Check if player wants to quit
    if user_play != "y":
        print("If you insist... Good luck missing out on all this money!")
        break

    # Generate the spin
    current_spin = [random.choice(reel) for reel in REELS]

    # Display the spin
    print("----------------")
    print(f"| {' | '.join(current_spin)} |")
    print("----------------")

    # Check if all symbols match
    if len(set(current_spin)) == 1:
        balance += 500
        print(f"You win! You won $500 and your current balance is: ${balance}")
    else:
        balance -= 200
        print(f"You lose! You lost $200 and your current balance is: ${balance}")

if balance < 200:
    print("Sorry, you have no more money left in your account!")
    print(" ")

print("Thanks for playing! Hope it was a fun experience")

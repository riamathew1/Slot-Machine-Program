# Pokies
# Ria 25/2/26

# Importing random function
import random

# Set the symbols in a 2D list
REELS = [
    ["😊", "🍔", "🚀"],
    ["🍔", "🤕", "🚀"],
    ["😊", "🍔", "🤕"]
]

# Greet the user to the program
print("Welcome to the slot machine!\n")

# Display the preview of the symbols
print("+--+----+--+")
for reel in REELS:
    print(" | ".join(reel))
print("+--+----+--+")

# Explain rules of program to user
print("\nYou will come across a face that shows 9 symbols.")
print("Get three matching symbols in the middle row and you win $500!")
print("If none of the symbols match you lose $200. Good luck!\n")

# Set 'user play' to "y" so the loops runs automatically
user_play = "y"

# Let user start with a balance of $100000
balance = 1000
# Using while loop so the user can play as long as they have more than $200
# Asking if user wants to play before generating slot machine spin
while balance >= 200:
    user_play = input(f"You currently have ${balance}. Spin for $500? y/n  ").lower().strip()

    # Check if player wants to quit
    if user_play != "y":
        print("If you insist... Good luck missing out on all this money!")
        break

    # Generate the spin using nested list comprehensions for efficiency
    grid = [[random.choice(reel) for _ in range(3)] for reel in REELS]

    # Display the 3x3 grid row by row
    print("+----+----+----+")
    for row in range(3):
        line = [column[row] for column in grid]
        print(f"| {' | '.join(line)} |")
    print("+----+----+----+")

    # Define the 'middle row' and check if the symbols match for a win
    middle_row = [grid[0][1], grid[1][1], grid[2][1]]
    
    # Check if all symbols match
    if len(set(middle_row)) == 1:
        balance += 500
        print(f"You win! You won $500 and your current balance is: ${balance}")
    else:
        balance -= 200
        print(f"You lose! You lost $200 and your current balance is: ${balance}")

# Once user's balance is less than $200 they can no longer continue
if balance < 200:
    print("Sorry, you have no more money left in your account!")
    print(" ")

# User has run out of money in their balance so the game is over
print("Thanks for playing! Hope it was a fun experience.")

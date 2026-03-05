# Pokies
# Ria 25/2/26

# Importing random function
import random

# Set the symbols in a 2D list
REELS = [
    ["😊", "🍔", "🚀"],
    ["🍔", "🤕", "🚀"],
    ["🚀", "🍔", "🤕"]
]

# Greet the user to the program
print("Welcome to the slot machine!\n")

# Display the preview of the symbols
print("+----+----+----+")
for row in range(3):
    display = [column[row] for column in REELS]
    print(f"| {' | '.join(display)} |")
print("+----+----+----+")

# Explain rules of program to user
print("\nYou will come across a face that shows 9 symbols.")
print("Get three matching symbols in a horizontal or diagonal row and you win $500!")
print("If none of the symbols match you lose $200. Good luck!\n")

# Set 'user play' to "y" so the loops runs automatically
user_play = "y"

# Let user start with a balance of $10000
balance = 10000

# Using while loop so the user can play as long as they have more than $200
# Asking if user wants to play before generating slot machine spin
while balance >= 200:
    user_play = input(f"You currently have ${balance}. Spin to win? y/n  ").lower().strip()

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

    #Define the top, bottom and middle rows
    top_row = [grid[0][0], grid[1][0], grid[2][0]]
    middle_row = [grid[0][1], grid[1][1], grid[2][1]]
    bottom_row = [grid[0][2], grid[1][2], grid[2][2]]

    #Define both the winning diagonal row combinations
    diag1 = [grid[0][0], grid[1][1], grid[2][2]]
    diag2 = [grid[0][2], grid[1][1], grid[2][0]]
    
    # Check if all symbols match
    if len(set(top_row)) == 1 or len(set(middle_row)) == 1 or len(set(bottom_row)) == 1:
        balance += 500
        print("ROW MATCH! You've won won $500!")
    elif len(set(diag1)) == 1 or len(set(diag2)) == 1:
        balance += 1000
        print("DIAGONAL MATCH! You've won $1000!")
    else:
        balance -= 200
        print("No matches! You lost $200!")

# Once user's balance is less than $200 they can no longer continue
if balance < 200:
    print("Sorry, you have no more money left in your account!")
    print(" ")

# User has run out of money in their balance so the game is over
print(" ")
print("Thanks for playing! Hope it was a fun experience.")

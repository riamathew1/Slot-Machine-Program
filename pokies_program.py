# Pokies
# Ria 25/2/26

# Importing random function
import random

# Set the symbols in a 2D list
REELS = [
    ["😊", "🍔", "🚀"],
    ["🍔", "🤕", "🚀"],
    ["🚀", "🍔", "🤕"]]

# Generate the spin
def generate_spin():
    grid = [random.choice(reel) for reel in REELS]

    # Display the 3x3 grid row by row
    print("+----+----+----+")
    print(f"| {' | '.join(grid)} |")
    print("+----+----+----+")
    return grid

# Winning line checker
def winning_line(grid):
    top_row = [grid[0][0], grid[1][0], grid[2][0]]
    middle_row = [grid[0][1], grid[1][1], grid[2][1]]
    bottom_row = [grid[0][2], grid[1][2], grid[2][2]]

    diag1 = [grid[0][0], grid[1][1], grid[2][2]]
    diag2 = [grid[0][2], grid[1][1], grid[2][0]]
    
    if len(set(top_row)) == 1 or len(set(middle_row)) == 1 or len(set(bottom_row)) == 1:
        print("ROW MATCH! You've won won $500!")
        return 500
    elif len(set(diag1)) == 1 or len(set(diag2)) == 1:
        print("DIAGONAL MATCH! You've won $1000!")
        return 1000
    else:
        print("No matches! You lost $200!")
        return -200
        return grid


# Main function
def main():
    balance = 1000
    print("Welcome to the slot machine!\n")
    print("+----+----+----+")
    for row in range(3):
        display = [column[row] for column in REELS]
        print(f"| {' | '.join(display)} |")
    print("+----+----+----+")
    print("\nYou will come across a face that shows 9 symbols.")
    print("Get three matching symbols in a horizontal or diagonal row and you win $500!")
    print("If none of the symbols match you lose $200. Good luck!\n")

    while balance >= 200:
        user_play = input(f"You currently have ${balance}. Spin to play? y/n: ")

        if user_play != "y":
            print("If you insist... Good luck missing out on all this money!")
            break
        
        grid = generate_spin()
        result = winning_line(grid)
        balance += result
        
    if balance < 200:
        print("Sorry, you have no more money left in your account!")
        print(" ")

    print(" ")
    print("Your final balance is {}".format(balance))
    print("Thanks for playing!")

main()

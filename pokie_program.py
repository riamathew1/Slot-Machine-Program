# Pokies
# Ria 25/2/26

# Importing random function
import random

# Global Constants
REELS = [
    ["😊", "🍔", "🚀"],
    ["🍔", "🤕", "🚀"],
    ["🚀", "🍔", "🤕"]]
SPIN_COST = 200
ROW_PRIZE = 500
COLUMN_PRIZE = 500
DIAGONAL_PRIZE = 1000
STARTING_BALANCE = 1000

def generate_spin():
    """
    Simulates a spin by shuffling each reel and returning as a 2D grid.
    """
    grid = []
    for reel in REELS:
        column = random.sample(reel, len(reel))     # random.sample() creates a unique shuffle based on reel length
        grid.append(column)
    return grid


def display_grid(grid):
    """
    Prints a formatted visual version of the grid.
    """
    size = len(grid)

    # Create a top border based on size of grid
    border = "+----" * size + "+"
    print(border)
    
    for row in range(size):
        row_string = "| "
        for column in range(size):
            row_string += grid[column][row] + " | "
        print(row_string)

    print(border)
    return grid


def check_all_wins(grid):
    """
    Checks the grid for matching rows, columns or diagonals.
    """
    size = len(grid)
    total_payout = 0

    # Check for winning rows (horizontal)
    for row in range(size):
        current_row_symbols = []
        for column in range(size):
            symbol = grid[column][row]
            current_row_symbols.append(symbol)

        # Using set() to see if all symbols in the row are identical
        if len(set(current_row_symbols)) == 1:
            print("ROW MATCH! You win ${}".format(ROW_PRIZE))
            total_payout += ROW_PRIZE
    
    # Check for winning columns (vertical)
    for column in range(size):
        # Specifically looks at vertical reels
        current_column = grid[column]
        if len(set(current_column)) == 1:
            print("COLUMN MATCH! You have won ${}!".format(COLUMN_PRIZE))
            total_payout += COLUMN_PRIZE

    # Check for winning diagonal rows
    diagonal_one = []
    diagonal_two = []
    for i in range(size):
        diagonal_one.append(grid[i][i])     # Checks from top-left to bottom-right
        diagonal_two.append(grid[i][size - 1 - i])      # Checks from top-right to bottom-left

    if len(set(diagonal_one)) == 1:
        print("DIAGONAL MATCH! You have won ${}!".format(DIAGONAL_PRIZE))
        total_payout += DIAGONAL_PRIZE

    if len(set(diagonal_two)) == 1:
        print("DIAGONAL MATCH! You have won ${}!".format(DIAGONAL_PRIZE))
        total_payout += DIAGONAL_PRIZE

    # Calculate final balance result for the spin
    if total_payout > 0:
        return total_payout
    else:
        print("No matches! You lost ${}!".format(SPIN_COST))
        return -SPIN_COST

        
def main():
    """
    Manages game structure, handles user input and tracks player profile.
    """
    # Start player profile
    name_input = input("What is your name? ")
    location_input = input("Where do you live? ")

    balance = STARTING_BALANCE
    player_profile = {
        "name": name_input,
        "location": location_input,
        "high_score": STARTING_BALANCE,
        "lifetime_losses": 0.0
    }
   
    print("Hello {} from {} and welcome to the slot machine!\n".format(player_profile['name'], player_profile['location']))
    initial_grid = generate_spin()
    display_grid(initial_grid)
    print("Get three matching symbols in a horizontal or diagonal row to win!")
    print("Rows = ${} | Columns = ${} | Diagonals = ${} | No match = -${}\n".format(ROW_PRIZE, COLUMN_PRIZE, DIAGONAL_PRIZE, SPIN_COST))

    # Main game loop
    while balance >= SPIN_COST:
        user_play = input("You currently have ${}. Spin to play? y/n: ".format(balance)).lower().strip()

        if user_play != "y":
            print("If you insist... Good luck missing out on all this money!")
            break

        # Generate the spin and check for wins
        grid = generate_spin()
        display_grid(grid)
        result = check_all_wins(grid)

        # Update balance and player profile stats
        balance += result

        # Track lifetime losses
        if result < 0:
            player_profile['lifetime_losses'] += abs(result)

        # Track high score
        if balance > player_profile['high_score']:
            player_profile['high_score'] = balance
        
    # Game over summary
    if balance < SPIN_COST:
        print("Sorry, you have no more money left in your account!")
        print(" ")

    print("\n--- Final Results --- ")
    print("Final balance is: ${}".format(balance))
    print("High Score: {}".format(player_profile['high_score']))
    print("Total lost: ${}".format(player_profile['lifetime_losses']))
    print("Thanks for playing!")

# Start program
if __name__ == "__main__":
    main()

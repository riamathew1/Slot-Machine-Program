"""Slot machine program that receives input from user, and generates spins."""

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
WHALE_THRESHOLD = 500


def get_valid_string(prompt):
    """Ensure the user enters a non-empty string with letters only."""
    while True:
        value = input(prompt).strip()
        if len(value) < 1:
            print("Input cannot be empty.")
        elif not value.replace(" ", "").isalpha():
            # Allows spaces for city names
            print("Please use letters only.")
        else:
            return value.title()


def get_valid_bet(balance):
    """Prompt user for a bet and check against their balance."""
    while True:
        try:
            bet = int(input(f"\nBetting amount - (Balance: ${balance}): "))
            if bet > balance:
                print(f"You only have ${balance}. Enter a lower bet!")
            elif bet <= 0:
                print("You must bet at least $1.")
            else:
                return bet
        except ValueError:
            print("Invalid input. Please enter a whole number.")


def generate_spin():
    """Simulate a spin by shuffling each reel and returning as a 2D grid."""
    grid = []

    for reel in REELS:
        # random.sample() creates a unique shuffle based on reel length
        column = random.sample(reel, len(reel))
        grid.append(column)
    return grid


def display_grid(grid):
    """Print a formatted visual version of the grid."""
    size = len(grid)

    # Create a top border based on size of grid
    border = "+----" * size + "+"
    print(border)

    # Format row contents from the column-major grid structure
    for row in range(size):
        row_string = "| "
        for column in range(size):
            row_string += grid[column][row] + " | "
        print(row_string)

    print(border)
    return grid


def check_all_wins(grid):
    """Check the grid for matching rows, columns or diagonals."""
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
        # Checks from top-left to bottom-right
        diagonal_one.append(grid[i][i])
        # Checks from top-right to bottom-left
        diagonal_two.append(grid[i][size - 1 - i])

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
        return 0


def check_marketing_status(player_profile):
    """Target ads if user is a whale and encourage them to keep betting."""
    if player_profile['lifetime_losses'] >= WHALE_THRESHOLD:
        print("Triple your credits and add more money to bet!")
        player_profile['target_ads'] = True
    else:
        print("Keep climbing up the leaderboard to win money!")
        player_profile['target_ads'] = False


def main():
    """Manage game structure, handle user input and track player profile."""
    # Start player profile
    print("--- Slot Machine ---")
    print("Welcome to the slot machine!\n")
    name = get_valid_string("What is your name? ")
    location = get_valid_string("Where do you live? ")

    balance = STARTING_BALANCE
    player_profile = {
        "name": name,
        "location": location,
        "high_score": 0,
        "lifetime_losses": 0.0,
        "target_ads": False
    }

    print(" ")
    print(f"Hello {player_profile['name']} from {player_profile['location']}!")
    initial_grid = generate_spin()
    display_grid(initial_grid)
    print("Get three matching symbols in a horizontal or diagonal row to win!")

    line_winners = (
                    f"Rows = ${ROW_PRIZE} | "
                    f"Columns = ${COLUMN_PRIZE} | "
                    f"Diagonals = ${DIAGONAL_PRIZE} | "
                    f"No match = -${SPIN_COST}\n"
    )
    print(line_winners)

    bet = 0

    # Main game loop
    while balance >= bet:
        prompt = (f"You currently have ${balance}.\n"
                  "Spin to play? y/n: ")
        user_play = input(prompt).lower().strip()

        if user_play != "y":
            print("If you insist... Good luck missing out on all this money!")
            break

        bet = get_valid_bet(balance)

        # Update balance and player profile stats
        balance -= bet
        player_profile['lifetime_losses'] += bet

        # Generate the spin and check for wins
        grid = generate_spin()
        display_grid(grid)
        payout = check_all_wins(grid)

        # Add payout back to balance
        balance += payout

        # Update high score
        if balance > player_profile['high_score']:
            player_profile['high_score'] = balance

        # Check if user is a whale and target ads
        check_marketing_status(player_profile)

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

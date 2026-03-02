# Pokies
# Ria 25/2/26

# Import random module
import random

# List for slot symbols 
REELS = [
  ["😊", "🍔", "🚀",],
  ["🍔", "🤕", "🚀"],
  ["😊", "🍔", "🤕"]]

# Greet the user and ask if they would like to play
print("Welcome to the slot machine!")
print(" ")
print("""You will come across a face that shows 9 symbols.
         Get three matching symbols in the middle row and you
         win $200! If none of the symbols match you end up losing
         $500. Good luck!""")
print(" ")
user_play = input("Would you like to spin the machine? y/n")

# Generate the spin (list comprehension for flexibility)
while user_play == "y":
    current_spin = [random.choice(reel) for reel in REELS]

# Display the spin
    print("----------------")
    print(f"| {' | '.join(current_spin)} |")
    print("----------------")

# Set inside an 'if statement' to check if the symbols in the reel are the same
    if len(set(current_spin)) == 1: 
        print("You win!")
        user_play = input("Would you like to continue playing? y/n")
    else:
        print("You lose!")
        

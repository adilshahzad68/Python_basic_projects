# dice_rolling_game

# Loop
# Ask: roll the dice?
# If user enters y
# Generate two random numbers
# Print them
# If user enters.n
# Print thank you message
# Terminate
# Else
# Print invalid choice

import random

while True:                                         # Loop
    choice = input("Roll the dice?(y/n): ").lower()  # Ask: roll the dice?
    if choice == 'y':                                  # If user enters y
        # Generate two random numbers
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        print(f'({die1},{die2})')                        # Print them
    elif choice == 'n':                                 # If user enters.n
        print('Thanks for playing')                 # Print thank you message
        break                                        # Terminate
    else:                                           # Else
        print('Invalid choice')                   # Print invalid choice

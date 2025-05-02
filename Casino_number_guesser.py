#!/usr/bin/env python3

# Created By: Tony G

# Date: 2025-04-08.

# Casino number guessing game.

import random

def main():
    # Start of the program.
    print("Hello, what is your name?")
    name = input()

    while True:
        print(f"Alright, {name}, do you have money to spend in the casino (Y/N)?")
        response = input()

        if (
            response == "N"
            or response == "n"
            or response == "No"
            or response == "no"
            or response == "NO"
        ):
            print(
                "Broke bum. Luckily, I am feeling generous, so I am willing to lend you 100 chips. "
                "However, I am expecting repayment, with interest."
            )
        elif (
            response == "Y"
            or response == "y"
            or response == "Yes"
            or response == "yes"
            or response == "YES"
        ):
            while True:
                print("Are you sure?")
                confirmation = input()

                if (
                    confirmation == "N"
                    or confirmation == "n"
                    or confirmation == "No"
                    or confirmation == "no"
                    or confirmation == "NO"
                ):
                    print(
                        "Broke bum. Luckily, I am feeling generous, so I am willing to lend you 100 chips. "
                        "However, I am expecting repayment, with interest."
                    )
                    break
                elif (
                    confirmation == "Y"
                    or confirmation == "y"
                    or confirmation == "Yes"
                    or confirmation == "yes"
                    or confirmation == "YES"
                ):
                    print("Alright, let's proceed.")
                    break
                else:
                    print("Invalid response. Please answer with Y/N.")
        else:
            print("Invalid response. Please answer with Y/N.")
            continue

        # Game logic starts here
        while True:
            print("Do you want to play 'guess the number' (Y/N)?")
            play_response = input()

            if (
                play_response == "Y"
                or play_response == "y"
                or play_response == "Yes"
                or play_response == "yes"
                or play_response == "YES"
            ):
                # Initialize game variables
                chips = 100
                cost = 10
                reward = 50
                luck = 10
                level = 1

                # Display game details
                print(f"You have {chips} chips.")
                print(f"Entry fee: {cost} chips.")
                print(f"Reward: {reward} chips.")
                print(f"Chances of winning: 1 in {luck}.")

                # Generate random number
                random_number = random.randint(1, luck)

                while True:
                    print(f"Please guess a number between 1 and {luck}")
                    guess = input()

                    # Validate input
                    if not guess.isdigit():
                        print("Invalid input. Please enter a valid number.")
                        continue

                    # Convert valid input to integer
                    guess = int(guess)
                    chips -= cost

                    if chips < cost:
                        print("You have run out of chips. The game is over.")
                        return  # End the program when the user runs out of chips

                    if guess == random_number:
                        print("I can't believe you won, GET OUT!!!")
                        chips += reward
                        return  # End the program when the user wins
                    else:
                        print("That was not it, try again.")
            elif (
                play_response == "N"
                or play_response == "n"
                or play_response == "No"
                or play_response == "no"
                or play_response == "NO"
            ):
                while True:
                    print("Are you sure?")
                    confirmation = input()

                    if (
                        confirmation == "Y"
                        or confirmation == "y"
                        or confirmation == "Yes"
                        or confirmation == "yes"
                        or confirmation == "YES"
                    ):
                        break
                    elif (
                        confirmation == "N"
                        or confirmation == "n"
                        or confirmation == "No"
                        or confirmation == "no"
                        or confirmation == "NO"
                    ):
                        continue
                    else:
                        print("Invalid response. Please answer with Y/N.")
            else:
                print("Invalid response. Please answer with Y/N.")


if __name__ == "__main__":
    main()

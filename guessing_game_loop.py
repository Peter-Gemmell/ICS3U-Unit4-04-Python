#!/usr/bin/env python3

# Created by Peter Gemmell
# Created on March 2022
# This program calculates the circumference of a circle using constants

import random


def main():
    # this function is the game

    # input, process & output
    mystery_number = random.randint(0, 9)  # a number between 0-9
    while True:
        try:
            number_guess_string = input("Guess a number between 0-9: ")
            guess_number = int(number_guess_string)
            if guess_number == mystery_number:
                print("\nYou guessed correctly!")
                break
            else:
                if guess_number > mystery_number:
                    print("That number is too high, guess lower.")
                else:
                    print("That number is too low, guess higher.")
        except Exception:
            print("That was not a integer from 0-9.")

    print("\nDone.")


if __name__ == "__main__":
    main()

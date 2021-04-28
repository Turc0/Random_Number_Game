import random
import time

"""
This program is game that generates a random number for the user 
to guess. The user will have 5 chances to guess a number between
0 - 100. 
"""


def start_game():
    print("Welcome to my random number guessing game!")

    start = input("When you are ready to play, enter 'Ready': \n")

    if start != 'Ready':
        print("Please enter 'Ready' ")
        start_game()


def play_game():
    num_of_guesses = 0
    print("Generating random value between 0 and 100...")
    time.sleep(5)
    random_num = random.randint(0, 100)
    print("Let's play! You only have 5 guesses!")

    for x in range(5):
        guess = int(input("Please enter your guess: "))

        if int(guess) == random_num:
            print(f"You guessed the right value, {random_num} in {num_of_guesses} turns!\n")
            break
        elif x == 4:
            print("You ran out guesses but you can try again!")
            print(f"The correct number was {random_num}\n")

            break
        else:
            if guess < random_num:
                print("Guess again but higher!\n")
            else:
                print("Guess again but lower!\n")

            num_of_guesses += 1


start_game()
play_game()

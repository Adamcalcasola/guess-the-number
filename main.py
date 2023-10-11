from art import logo
import random

def guess_the_number():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if difficulty == 'easy':
        attempts = 10
    elif difficulty == 'hard':
        attempts = 5
    else:
        print("Invalid command")
        attempts = 0

    number = random.randint(1, 100)

    while attempts > 0:
        if attempts > 1:
            print(f"You have {attempts} attempts remaining to guess the number.")
        else:
            print(f"You have {attempts} more attempt to guess the number!")
        guess = int(input("Make a guess: "))
        attempts -= 1
        if guess == number:
            print("You Win!")
            break
        elif guess > number:
            print("Too high.")
        elif guess < number:
            print("Too low.")

        if attempts > 0:
            print("Guess again.")
        else:
            print("You've run out of guesses, you lose.")

    play_again = input("Want to play again? Type 'y' or 'n': ")
    if play_again == "y":
        guess_the_number()
    else:
        return
    
guess_the_number()

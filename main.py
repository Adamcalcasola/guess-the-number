from art import logo
import random

def difficulty():
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if difficulty == 'easy':
        return 10
    elif difficulty == 'hard':
        return 5
    else:
        print("Invalid command")
        return 0
    
def check_answer(attempts, number, guess):
    if guess > number:
        print("Too high.")
        return attempts - 1
    elif guess < number:
        print("Too low.")
        return attempts - 1
    else:
        print(f"You guessed the secret number, {number}!")
        print("You Win!")

def guess_the_number():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    attempts = difficulty()
    number = random.randint(1, 100)
    guess = 0

    while guess != number and attempts > 0:
        if attempts > 1:
            print(f"You have {attempts} attempts remaining to guess the number.")
        else:
            print(f"You have {attempts} more attempt to guess the number!")
        
        guess = int(input("Make a guess: "))
        
        attempts = check_answer(attempts, number, guess)

        if attempts == 0:
            print("You've run out of guesses, you lose.")
            play_again = input("Want to play again? Type 'y' or 'n': ")
            if play_again == "y":
                guess_the_number()
                return
            else:
                return
        elif guess != number:
            print("Guess again.")

guess_the_number()
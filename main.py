from art import logo
import random

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
    print(f"You have {attempts} attempts remaining to guess the number.")
    guess = int(input("Make a guess:"))
    if guess == number:
        print("You Win!")
    elif guess > number:
        print("Too high.\nGuess again.")
    elif guess < number:
        print("Too low.\nGuess again.")

print("You've run out of guesses, you lose.")
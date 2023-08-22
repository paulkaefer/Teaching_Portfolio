# This line is a comment!

# we need to import the random module for this to work:
import random

# generate a random integer from 1 to 100:
random_number = random.randint(1, 100)

guessed = False
while (guessed == False):
    guess = int(input("Guess a number (1-100): "))
    if guess == random_number:
        print("Correct!")
        break
    elif guess < random_number:
        print("Too low. Try again!")
    else:
        print("Too high. Try again!")


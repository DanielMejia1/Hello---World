"""
Document
i
"""
import random

secret = random.randint (1,99) # Generate ramdom integers between 1 and 99

guess = 0
tries = 0
print("Can you gu1ess my number?")
print(" My number is an integer between 1 and 99")

while guess != secret and tries < 6 :
    print("What's your name")
    guess = int(imput())
    if guess < secret:
        print("Too Low")
    elif guess > secret:
        print("Too high")

tries = tries + 1


if guess == secret:
    print("You got it! Bravoooo!")
else  :
    print("Nope! Try again please!")
    print("The secret number is secret = ", secret)
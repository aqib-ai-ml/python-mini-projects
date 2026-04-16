import random

print("Welcome to the Number Guessing Game!")
print("Guess a number between 1 and 100")

number = random.randint(1, 100)

guess = int(input("Enter your guess: "))

while guess!= number:
    if guess<number:
        print("Number too low!")
    else:
        print("Number too high")
    guess = int(input("Try again:- "))
print(f"Congratulations!!! You found the number, it was {number}")
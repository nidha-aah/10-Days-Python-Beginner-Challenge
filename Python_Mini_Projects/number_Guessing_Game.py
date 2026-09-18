import random

secret_number = random.randint(1,10)

guess = int(input("Guess the number (1-10): "))

if guess == secret_number:
    print("Correct")
elif guess > secret_number:
    print("Too Highhhhh")
else:
    print("Too low!")    
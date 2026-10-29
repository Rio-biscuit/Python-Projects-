
import random

secret_number = random.randint(1, 10)
attempts = 3

print("Welcome to the Number Guessing Game!")
print("I have selected a number between 1 and 10.")
print("You have 3 attempts to guess it.")

while attempts > 0:
    guess = int(input("Enter your guess: "))

    if guess == secret_number:
        print("Congratulations! You guessed the correct number!")
        break
    else:
        attempts -= 1

        if secret_number % 3 == 0 and attempts > 0:
            print("Wrong guess! Try again.")
            print("Attempts remaining:", attempts)
            print("Hint: The secret number is divisible by 3.")

        elif secret_number % 2 == 0 and attempts > 0:
            print("Wrong guess! Try again.")
            print("Attempts remaining:", attempts)
            print("Hint: The secret number is divisible by 2.")

        elif secret_number == 1 and attempts > 0:
            print("Wrong guess! Try again.")
            print("Attempts remaining:", attempts)
            print("Hint: I love card games!")

        elif attempts > 0:
            print("Wrong guess! Try again.")
            print("Attempts remaining:", attempts)

        if attempts == 0:
            print("Game over! You ran out of attempts.")
            print("The secret number was:", secret_number)


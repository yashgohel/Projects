import random


def number_guessing():
    print("Welcome to number guessing game!")
    random_number = random.randint(1, 20)
    attempt = 0

    while True:
        user_input = input('Enter your guess or "exit" to quit: ')
        if user_input.lower() == "exit":
            print("Thank you!")
            break
        try:
            guessed_number = int(user_input)
            if guessed_number < 1 or guessed_number > 20:
                print("Please guess between 1-20.")
                continue
            attempt += 1
            if guessed_number > random_number:
                print("Too high! Please guess again!")
            elif guessed_number < random_number:
                print("Too low! Please guess again.")
            else:
                print(
                    f"Bravo! You guessed correctly in {attempt} attempts!!! The number is {random_number}."
                )
                break
        except ValueError:
            print('Please enter correct number from 1-20 or "exit"....')


if __name__ == "__main__":
    number_guessing()

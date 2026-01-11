import random

print("Welcome to Rock, Paper, Scissors Game!")

choices = ["rock", "paper", "scissors"]
while True:
    user_c = input("Enter your choice or else type 'exit' to end the game: ")
    if user_c == "exit":
        print("Thanks to play! have a good day ahead!")
        break
    if user_c not in choices:
        print("Invalid choice. Please try with correct choice.")
        continue
    computer_c = random.choice(choices)
    print("Computer choice is: ", computer_c)
    if user_c == computer_c:
        print("Opps! It's a Tie!")
    elif (
        (user_c == "rock" and computer_c == "scissors")
        or (user_c == "scissors" and computer_c == "paper")
        or (user_c == "paper" and computer_c == "rock")
    ):
        print("Bingo! You win!")
    else:
        print("You Lose! Better luck next time!")

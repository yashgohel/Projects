questions = [
    ["Who is Sachin Tendulkar?", "Actor", "Footballer", "Cricketer", "Astronaut", 3],
    ["Where is Statue of Unity?", "Paris", "Bharuch", "France", "Vadodara", 2],
    ["What is the capital of Gujarat?", "Ahmedabad", "Delhi", "Vadodara", "Gandhinagar", 4]
]
se = ["first", "second", "last"]
print("Welcome to Who wants to be a millionair game!\nMy name is Amitabh Bacchan.\nLet's start the game!")
prizes = [1000, 2000, 3000]
i = 0
for q in questions:
    print(f"Here is the {se[i]} question: {q[0]}")
    print(f"a. {q[1]}")
    print(f"b. {q[2]}")
    print(f"c. {q[3]}")
    print(f"d. {q[4]}")

    a = int(input("Enter your answer (1 for a, 2 for b, 3 for c, 4 for d): "))
    if q[5] == a:
        print("Your answer is correct! ")
    else:
        print(f"The correct answer was {q[5]}.\nBetter luck next time!")
        break
    print(f"You won the prize: {prizes[i]}")
    i = i+1
        
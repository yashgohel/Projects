try: 
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    print("What kind of performance you want to perform: add(+), sub(-), mul(*), div(/), mod(%), exp(**), floordiv(//)?")
    o = input("Enter operation: ")

    match o:
        case "+":
            print(f"The result is: {a + b}")
        case "-":
            print(f"The result is: {a - b}")
        case "*":
            print(f"The result is: {a * b}")
        case "/":
            print(f"The result is: {a / b}")
        case "%":
            print(f"The result is: {a % b}")
        case "//":
            print(f"The result is: {a // b}")
        case "**":
            print(f"The result is: {a ** b}")
        case default:
            print("Please enter the operation from the mentioned list.")
except Exception as e:
    print("Print a valid value of numbers!!!")


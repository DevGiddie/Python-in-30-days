def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2

print("Welcome to the Calculator Program!")

while True:
    print("Select an operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == '5':
        print("Exiting the program. Goodbye!")
        break

    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    if choice == '1':
        result = add(num1, num2)
        print("The result is:", result)
    elif choice == '2':
        result = subtract(num1, num2)
        print("The result is:", result)
    elif choice == '3':
        result = multiply(num1, num2)
        print("The result is:", result)
    elif choice == '4':
        if num2 == 0:
            print("Error: Division by zero is not allowed.")
        else:
            result = divide(num1, num2)
            print("The result is:", result)
    else:
        print("Invalid choice. Please try again.")

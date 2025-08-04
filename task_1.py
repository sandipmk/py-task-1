# Calculator CLI program

#functions for basic arithmetic operations
def addition(x, y):
    return x + y

def subtraction(x, y):
    return x - y

def multiplication(x, y):
    return x * y

def division(x, y):
    if y == 0:
        return "Error: Division by zero"
    return x / y

#main function to run the calculator
def main():
    print("---Calculator---")
    print("")
    while True:
        print("\nChoose operation:")
        print(" (+) --> Addition")
        print(" (-) --> Subtraction")
        print(" (*) --> Multiplication")
        print(" (/) --> Division")
        print(" (0) --> Exit")

        choice = input("Enter your choice (+/-/*//0): ")
        # Check if the user wants to exit
        if choice == '0':
            print("Exiting calculator....")
            break
        # Check if the user selected a valid operation
        if choice in ['+', '-', '*', '/']:

            # Get user input for numbers
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("Invalid input. Please enter numeric values.")
                continue

            # Perform the selected operation
            if choice == '+':
                print(f"{num1} + {num2} = {addition(num1, num2)}")
            elif choice == '-':
                print(f"{num1} - {num2} = {subtraction(num1, num2)}")
            elif choice == '*':
                print(f"{num1} * {num2} = {multiplication(num1, num2)}")
            elif choice == '/':
                print(f"{num1} / {num2} = {division(num1, num2)}")
        else:
            print("Invalid choice...")

# run directly if this script is executed
if __name__ == "__main__":
    main()

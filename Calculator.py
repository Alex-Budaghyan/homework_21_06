def calculator():
    while True:
        # Ask for user input
        num1 = float(input("Enter the first number: "))
        operator = input("Enter an operator (+, -, *, /) or 'exit': ")

        # Check if user wants to exit
        if operator.lower() == 'exit':
            print("Exiting the calculator...")
            break
        num2 = float(input("Enter the second number: "))
        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            result = num1 / num2
        else:
            print("Invalid operator! Please try again.")
            continue
        print("Result:", result)
        # print()


calculator()

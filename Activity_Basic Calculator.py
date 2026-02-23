# Basic Calculator (No .0 if whole number)

print("Select operation.")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

choice = input("Enter choice (1/2/3/4): ")

if choice in ('1', '2', '3', '4'):
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == '1':
        result = num1 + num2
        symbol = "+"
    elif choice == '2':
        result = num1 - num2
        symbol = "-"
    elif choice == '3':
        result = num1 * num2
        symbol = "*"
    elif choice == '4':
        if num2 == 0:
            print("Error: Cannot divide by zero.")
            exit()
        result = num1 / num2
        symbol = "/"

    if result.is_integer():
        result = int(result)

    print(f"{num1} {symbol} {num2} = {result}")

else:
    print("Invalid input. Please select 1, 2, 3, or 4.")
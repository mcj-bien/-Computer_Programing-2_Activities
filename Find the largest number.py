# Function to find the largest number
def find_largest(a, b, c):
    if a >= b and a >= c:
        return "A", a
    elif b >= a and b >= c:
        return "B", b
    else:
        return "C", c


# Get input from user
a = float(input("Enter your first number: "))
b = float(input("Enter your second number: "))
c = float(input("Enter your third number: "))

# Call the function
letter, largest = find_largest(a, b, c)

# Remove .0 if whole number
if largest.is_integer():
    largest = int(largest)

print(f"Letter {letter} is the largest number with a value of {largest}")
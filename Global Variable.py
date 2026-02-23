# Global variable
x = 300

print(f"Find the closest number to {x}")

# Input
a = int(input("Enter your first number: "))
b = int(input("Enter your second number: "))
c = int(input("Enter your third number: "))

# Compute distances
diff_a = abs(x - a)
diff_b = abs(x - b)
diff_c = abs(x - c)

# Find smallest difference
min_diff = min(diff_a, diff_b, diff_c)

# Check which is closest
if diff_a == min_diff and diff_b != min_diff and diff_c != min_diff:
    print(f"Letter A or {a} is the closest number to {x}")

elif diff_b == min_diff and diff_a != min_diff and diff_c != min_diff:
    print(f"Letter B or {b} is the closest number to {x}")

elif diff_c == min_diff and diff_a != min_diff and diff_b != min_diff:
    print(f"Letter C or {c} is the closest number to {x}")

elif diff_a == diff_b == diff_c:
    print("All numbers are equally close to", x)

elif diff_a == diff_b:
    print(f"Letter A ({a}) and Letter B ({b}) are equally closest to {x}")

elif diff_a == diff_c:
    print(f"Letter A ({a}) and Letter C ({c}) are equally closest to {x}")

else:
    print(f"Letter B ({b}) and Letter C ({c}) are equally closest to {x}")
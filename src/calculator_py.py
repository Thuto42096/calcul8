import math

def add(x, y):
    """Add two numbers."""
    return x + y

def subtract(x, y):
    """Subtract two numbers."""
    return x - y

def multiply(x, y):
    """Multiply two numbers."""
    return x * y

def divide(x, y):
    """Divide two numbers."""
    if y == 0:
        raise ValueError("Cannot divide by zero.")
    return x / y

def power(x, y):
    """Raise x to the power of y."""
    return x ** y

def square_root(x):
    """Return the square root of x."""
    if x < 0:
        raise ValueError("Cannot take the square root of a negative number.")
    return math.sqrt(x)

def percentage(x, total):
    """Calculate the percentage of x with respect to total."""
    if total == 0:
        raise ValueError("Total cannot be zero.")
    return (x / total) * 100

def main():
    print("====Simple Calculator====\n")
    print("Select an operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Power")
    print("6. Square Root")
    print("7. Percentage")

    choice = input("Select operation (1-7): ")

    if choice in ['1', '2', '3', '4', '5']:
        x = float(input("Enter first number: "))
        y = float(input("Enter second number: "))
        if choice == '1':
            print(f"Result: {add(x, y)}")
        elif choice == '2':
            print(f"Result: {subtract(x, y)}")
        elif choice == '3':
            print(f"Result: {multiply(x, y)}")
        elif choice == '4':
            print(f"Result: {divide(x, y)}")
        elif choice == '5':
            print(f"Result: {power(x, y)}")

    elif choice == '6':
        x = float(input("Enter number to find square root: "))
        print(f"Result: {square_root(x)}")

    elif choice == '7':
        x = float(input("Enter the part value: "))
        total = float(input("Enter the total value: "))
        print(f"Result: {percentage(x, total)}%")

    else:
        print("Invalid operation selected.")

if __name__ == "__main__":
    main()


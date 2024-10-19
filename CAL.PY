def add(a, b):
    """Add two numbers."""
    return a + b

def subtract(a, b):
    """Subtract two numbers."""
    return a - b

def multiply(a, b):
    """Multiply two numbers."""
    return a* b

def divide(a, b):
    """Divide two numbers."""
    if b == 0:
        raise ValueError("Cannot divide by zero!")
    return a / b

# Main program
def main():
    operations = {
        '1': add,
        '2': subtract,
        '3': multiply,
        '4': divide
    }
    print("Select any one from below:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    while True:
        choice = input("Enter any choice (1/2/3/4): ")
        if choice in operations:
            try:
                num1 = float(input("Enter your first number: "))
                num2 = float(input("Enter your second number: "))
                result = operations[choice](num1, num2)
                print(f"The result for input is: {result}")
            except ValueError as e:
                print(f"Invalid input: {e}")
            if input("Let's do next calculation? (yes/no): ").lower() == 'no':
                break
        else:
            print("Invalid input. Please try again.")

if __name__ == "__main__":
    main()
    
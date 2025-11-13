def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero!"
    return a / b

while True:
    print("\n=== Simple Calculator ===")
    print("Select operation:")
    print("1. Add (+)")
    print("2. Subtract (-)")
    print("3. Multiply (*)")
    print("4. Divide (/)")
    print("5. Exit")

    choice = input("Enter choice (1/2/3/4/5): ")

    if choice == '5' or choice.lower() == 'exit':
        print("Exiting calculator. Goodbye!")
        break

    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("Invalid input! Please enter numeric values.")
        continue
 
    if choice == '1':
        print(f"Result: {num1} + {num2} = {add(num1, num2)}")
    elif choice == '2':
        print(f"Result: {num1} - {num2} = {subtract(num1, num2)}")
    elif choice == '3':
        print(f"Result: {num1} * {num2} = {multiply(num1, num2)}")
    elif choice == '4':
        print(f"Result: {num1} / {num2} = {divide(num1, num2)}")
    else:
        print("Invalid choice! Please select 1-5.")
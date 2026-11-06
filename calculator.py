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

print("=== Simple Calculator ===")

while True:
    print("\n1. Add (+)")
    print("2. Subtract (-)")
    print("3. Multiply (*)")
    print("4. Divide (/)")
    print("5. Exit")

    choice = input("Choose option (1-5): ")

    if choice == "5":
        print("Calculator closed. Bye!")
        break

    if choice not in ["1", "2", "3", "4"]:
        print("Invalid choice! 1-5 kulla kodu.")
        continue

    num1 = float(input("First number: "))
    num2 = float(input("Second number: "))

    if choice == "1":
        print("Result:", add(num1, num2))
    elif choice == "2":
        print("Result:", subtract(num1, num2))
    elif choice == "3":
        print("Result:", multiply(num1, num2))
    elif choice == "4":
        print("Result:", divide(num1, num2))

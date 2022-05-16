# Inderpreet Singh
# Program: Basic Calculator
# Program make a simple calculator

# defining (add) function to perform addition of two numbers
def add(x, y):
    return x + y


# defining (Subtraction) function to perform addition of two numbers
def subtraction(x, y):
    return x - y


# defining (multiplication) function to perform x * y;
def multiply(x, y):
    return x * y


# defining (division) function to perform x/y:
def division(x, y):
    return x / y


# defining (exponential) function to perform x^y
def expon(x, y):
    return x ** y


print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
print("5 Exponential")

while True:
    # take input from the user
    choice = input("Enter choice: 1)/ 2) /3) /4) /5): ")

    if choice not in ('1', '2', '3', '4', '5'):
        print("invalid Input")
    # check if choice is one of the four options
    else:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtraction(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", division(num1, num2))

        elif choice == '5':
            print(num1, "/", num2, "=", expon(num1, num2))

        # check if user wants another calculation: If no Break otherwise restart the function
        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
            break

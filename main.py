# Program make a simple calculator
import html
import math
num1 = 0
num2 = 0
ans = 0

# This function adds two numbers
def add(x, y):
    return x + y

# This function subtracts two numbers
def subtract(x, y):
    return x - y

# This function multiplies two numbers
def multiply(x, y):
    return x * y

# This function divides two numbers
def divide(x, y):
    return x / y

# This function raises x to the yth num1 = 0
def exponent(x, y):
    return x ** y

def log (x, y):
    return math.log(x, y)

print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
print("5.Exponent")
print("6.Log")

while True:
    # take input from the user
    choice = input("Enter choice(1/2/3/4/5/6): ")

    if ans:
        num1 = ans
        num2 = float(input("Enter second number: "))
    else:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

    # check if choice is one of the four options
    if choice in ('1', '2', '3', '4', '5', '6'):

            if choice == '1':
                ans = add(num1, num2)
                print(num1, "+", num2, "=", ans)

            elif choice == '2':
                ans = subtract(num1, num2)
                print(num1, "-", num2, "=", ans)

            elif choice == '3':
                ans = multiply(num1, num2)
                print(num1, "X", num2, "=", ans)

            elif choice == '4':
                ans = divide(num1, num2)
                print(num1, html.unescape('&divide;'), num2, "=", ans)

            elif choice == '5':
                ans = exponent(num1, num2)
                print(num1, "^", num2, "=", ans)

            elif choice == '6':
                ans = log(num2, num1)
                print("log base", num1, "of", num2, "=", ans)

            # check if user wants another calculation
            # break the while loop if answer is no
            next_calculation = input("Let's do next calculation? (yes/no/useAnswer): ")
            if next_calculation == "useAnswer":
                num1 = ans

            if next_calculation == "yes":
                ans = 0

            if next_calculation == "no":
                break
    else:
        print("Invalid Input")

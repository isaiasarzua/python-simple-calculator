num1 = float(input("Enter first number: "))
operator = input("Enter operator: ")
num2 = float(input("Enter second number: "))

if operator == "+":
    print(num1 + num2)
elif operator == "-":
    print(num1 - num2)
elif operator == "/":
    print(num1 / num2)
elif operator == "*":
    print(num1 * num2)
else:
    print("Error: Invalid operator please use one of the following:\n"
          "+ for addition\n"
          "- for subtraction\n"
          "/ for division\n"
          "* for multiplication")
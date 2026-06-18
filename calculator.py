print("Simple Calculator")

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("Choose operation: +  -  *  /")
number = input("Enter operator: ")

if number == "+":
    print("Result:", num1 + num2)
elif number == "-":
    print("Result:", num1 - num2)
elif number == "*":
    print("Result:", num1 * num2)
elif number == "/":
    if num2 != 0:
        print("Result:", num1 / num2)
    else:
        print("Cannot divide by zero")
else:
    print("Invalid operator")

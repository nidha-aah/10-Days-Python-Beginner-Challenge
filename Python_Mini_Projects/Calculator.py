# calculator

num1 = float(input("Enter the first number : "))
num2 = float(input("Enter the second number : "))
operator = input("Enter operator (+, -, *, /): ")

if operator == "+":
    print("Result: ",num1 + num2)
elif operator == "-":
    print("Result: ",num1 - num2)
elif operator == "*" :
    print("Result: ",num1 * num2)
elif operator == "/":
    if num2 != 0:
        print("Result:", num1 / num2)
    else:
        print("Cannot divide by zero.")

else:
    print("Invalid operator.")

operator = input("Enter an Operator (+ - * /): ")
num1 = float(input("1st Number: "))
num2 = float(input("1st Number: "))

if operator == "+":
    result = num1 + num2
    print(result)
elif operator == "-":
    result = num1 - num2
    print(result)
elif operator == "*":
    result = num1 * num2
    print(result)
elif operator == "/":
    result = num1 / num2
    print(result)
else:
    print(f"{operator} isn't a valid operator")
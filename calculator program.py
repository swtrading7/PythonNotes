# Python Calc

operator = input("Enter an operator (+ - * /  %): ")
num1 = float(input("Enter 1st number: "))
num2 = float(input("Enter 2nd number: "))

print ( num1 + num2 )

if operator == "+":
    result = num1 + num2
    print(round(result, 3))
elif operator == "-":
    result = num1 - num2
    print(round(result, 3))
elif operator == "*":
    result = num1 * num2
    print(round(result,3))
elif operator == "/":
    result = num1 / num2
    print(round(result,3))
else: print("Invalid operator")

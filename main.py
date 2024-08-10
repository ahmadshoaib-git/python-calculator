def add(operand1, operand2):
    return operand1 + operand2

def subtract(operand1, operand2):
    return operand1 - operand2

def divide(operand1, operand2):
    return operand1 / operand2

def multiply(operand1, operand2):
    return operand1 * operand2

def operations(operand1, operand2, operator):
    equation = f"{operand1} {operator} {operand2} = "   
    if operator == '+':
        print(equation+str(add(operand1,operand2)))
    elif operator == '-':
        print(equation+str(subtract(operand1,operand2)))
    elif operator == '*':
        print(equation+str(multiply(operand1,operand2)))
    elif operator == '/':
        print(equation+str(divide(operand1,operand2)))
    pass

def calculator():
    print('''         _____________________
        |  _________________  |
        | | JO           0. | |
        | |_________________| |
        |  ___ ___ ___   ___  |
        | | 7 | 8 | 9 | | + | |
        | |___|___|___| |___| |
        | | 4 | 5 | 6 | | - | |
        | |___|___|___| |___| |
        | | 1 | 2 | 3 | | x | |
        | |___|___|___| |___| |
        | | . | 0 | = | | / | |
        | |___|___|___| |___| |
        |_____________________|''')
    operand1 = int(input("\nPlease enter first number: "))
    operand2 = int(input("Please enter second number: "))
    operator = input("Please enter operator (+ - / *): ")
    operations(operand1, operand2, operator)
    pass

while 1:
    calculator()
    userContinue = input("Do you want to perform more calculations? \nPress 'y' to continue and 'n' to exit\n> ")
    if userContinue != "y":
        break
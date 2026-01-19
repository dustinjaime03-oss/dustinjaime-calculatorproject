#Calculator Project 

#Adds numbers
def add(x, y):
    return x + y

#Subtracts numbers
def subtract(x, y):
    return x - y 

#Multiplies numbers
def multiply(x, y):
    return x * y

#Divides numbers
def divide(x, y):
    return x / y 

#raises x to the power of y
def exponent(x, y):
    return x ** y

#Asks user for an x value
x = float(input("Enter a value for x: "))

#asks user for operation
print("Choose an operation: +, -, *, /, ** ")
operation = input("Enter Operation: ")

#Asks user for y value
y = float(input("Enter a value for y: "))

#Performs Calculation based on user input for x, y and operation chosen and prints result
if operation == '+':
    result = add(x, y)
    print(f"Calculation: {x} + {y} = {result}")

elif operation == '-':
    result = subtract(x, y)
    print(f"Calculation: {x} - {y} = {result}")

elif operation == '*':
    result = multiply(x, y)
    print(f"Calculation: {x} * {y} = {result}")

elif operation == '/':
    
    result = divide(x, y)
    print(f"Calculation: {x} / {y}")

    if y == 0:
        print("Error:cannot divide by Zero")

    else:
        #Asks user if they want whole numbers or decimals
        mode = input("Do you want whole numbers(1) or decimals(2)? ")
        #Asks user if they want remainders
        remainder = input("Do you want remainders to be calculated? (yes/no) ")

#For whole numbers
        if mode == '1':
            Answer = int(x // y)
            print(f"Calculation: {int(x)} / {int(y)} = {Answer}")
            if remainder == 'yes':
                remainder = int(x % y)
                print(f"Remainder: {remainder}")

#For Decimals
        else:
            result = divide(x, y)
            print(f"Calculation: {x} / {y} = {result}")
            if remainder == 'yes':
                remainder = x % y

elif operation == '**':
    result = exponent(x, y)
    print(f"Calculation: {x} ** {y} = {result}")

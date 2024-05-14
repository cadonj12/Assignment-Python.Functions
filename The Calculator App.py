#Task 1

#Addition function
def add(x, y):
    return x + y

#Subtraction function
def subtract(x, y):
    return x - y

#Multiplication function
def multiply(x, y):
    return x * y

#Division function
def divide(x, y):
    return x / y


#Task 2
    
#Input numbers
number1 = float(input("Enter first number: "))
number2 = float(input("Enter second number: "))

#Choose an operation

print("Operations: \n1. Add \n2. Subtract \n3. Multiply \n4. Divide")
operation = input("Enter a number (1-4): ")

#Use if and elif statements for each operation
if operation == "1":
    print(f"{number1} + {number2} = {add(number1, number2)}")
elif operation == "2":
    print(f"{number1} - {number2} = {subtract(number1, number2)}")
elif operation == "3":
    print(f"{number1} * {number2} = {multiply(number1, number2)}")
elif operation == "4":
    print(f"{number1} / {number2} = {divide(number1, number2)}")
else:
    print("Invalid input. Type a number 1-4.")


#Task 3

#Addition function
def add(x, y):
    return x + y

#Subtraction function
def subtract(x, y):
    return x - y

#Multiplication function
def multiply(x, y):
    return x * y

#Division function
def divide(x, y):
#Add error message if denominator is 0
    if y == 0:
        return "Error, number does not exist!"    
    else:
        return x / y

#Input numbers
number1 = float(input("Enter first number: "))
number2 = float(input("Enter second number: "))

#Choose an operation

print("Operations: \n1. Add \n2. Subtract \n3. Multiply \n4. Divide")
operation = input("Enter a number (1-4): ")

#Use if and elif statements for each operation
if operation == "1":
    print(f"{number1} + {number2} = {add(number1, number2)}")
elif operation == "2":
    print(f"{number1} - {number2} = {subtract(number1, number2)}")
elif operation == "3":
    print(f"{number1} * {number2} = {multiply(number1, number2)}")
elif operation == "4":
    print(f"{number1} / {number2} = {divide(number1, number2)}")
else:
    print("Invalid input. Type a number 1-4.")
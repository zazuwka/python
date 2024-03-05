# Task is to write a pyhton program which to perform simple arithmetic operations (+, -, *, /)
# It should take 2 numbers as user input. Also, take a arithmetic operation as user input. 
# it should be done using function, so that when call it, it does the job for us. 
# Enter num 1
# Enter num 2
# which operation you want to perform? + - / *
# result

def calculator ():
    num1 = float(input("Emter first number: "))
    num2 = float(input("Emter second number: "))

    operation = (input ("Enter operation: +, -, /, *\n"))

    if operation == "+":
        return (num1 + num2)
    elif operation == "-":
        return (num1 - num2)
    elif operation == "/":
        return (num1 / num2)
    elif operation == "*":
        return (num1 * num2)
    else: print ("Wrong input")

var1 = calculator()
print (var1)









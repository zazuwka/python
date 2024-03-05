# user input is a function that alloww for a user to enter(input) some information
# when user input is taken by a function, it is stored inside a variable
# function saves the input in string format, and if you another data type, u have to use casting. 

first_name = input("What is your name? ")        #this one take input from the same line as message
last_name = input("What is your last name\n")   #this one takes input from the next line from message

print (f"Hello, {first_name} {last_name}")

var1 = input ("Enter a number: ")

print (type(var1))

#in order to convert str to, for example, integers, we use casting. 
num_var = int(var1)
print( type(num_var))

num1 = int(input("Enter a number which you want to be an integer: "))
print(num1)
print(type(num1))
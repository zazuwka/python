print (1)
print ("Kazien is a great bootcamp")

var1 = "test"
print(var1)

# Print out the solution to: (26 * 30 * 12) + - / *

##### Data types
# Integer - whole number
# Float - decimal number
# String - sequence of characters
# boolean - True, False

##### Variables
# Variables are containers for storing values. 

var1 = 10
var2 = 10.5
var3 = "some text"
var4 = True
Var5 = False

calculation_to_units = 24 * 60 * 60         # total number of seconds in 1 day (24hours)
print(calculation_to_units)

name_of_units = "seconds"

# 5 days are equal to XXXXX seconds

print (f"5 days are equal to {5 * calculation_to_units} seconds")
#this is how we concatenate string with other data/variables


#Functions - are used to make our code more dynamic. Essentially, the function is a block of code, and it is used to aboid repetition. 
# lets create a function that helmps us simplify code from line 31-38.
# functions take arguments as parameters, in paranthesies. There can be 1,2,3 and more arguments passed to a function.
def days_to_units(num_of_days):
    print (f"{num_of_days} days are equal to {num_of_days * calculation_to_units} seconds")

# in order to use the function, you have to call in your code by using the name of the function (without def).

days_to_units(10)
days_to_units(15)
days_to_units(20)
days_to_units(26)



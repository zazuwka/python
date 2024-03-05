# Create a python program, which takes user input, and then converts a number 
# to 1)days, 2)weeks, 3)month. Both the number and the proposed conversion unit 
# have to be user input. 

# Ex. Please enter the number of years:
#     Please choose which unit you want to convert to:
# 	1 - days
# 	2 - weeks
#   3 - month


var1 = int(input ("Please enter the number of years: "))
var2 = int(input ("""Please choose which unit you want to convert to
              1 - days
              2 - weeks
              3 - months\n"""))

if var2 == 1:
    print (f"{var1 * 365} days")
elif var2 == 2:
    print (f"{var1 * 52} weeks")
elif var2 == 3:
    print (f"{var1 * 12} months")
else:
    print("Wrong input, please try again!")
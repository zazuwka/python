# Calculation of cloud services prices
# Ask user to enter an hourly cost of running one server
# Ask the user to choose between calculating the monthly cost or the yearly cost
# Calculate and pring the estimated cost based on the user's selection 


hourly_cost = float(input("Please enter hourly cost of running a server: "))

choice = (input("""Please choose monthly or yearly cost: 
                   1 - monthly
                   2 - yearly
                   \n """))

if choice == "1":
    monthly_cost = hourly_cost * 24 * 30
    print (f"Monthly cost will be ${monthly_cost}")

elif choice == "2":
    yearly_cost = hourly_cost * 24 * 30 * 12
    print (f"Yearly cost will be ${yearly_cost}")
else:
    print ("Wrong choice")
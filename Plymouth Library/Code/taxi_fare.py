# This is the example from Figure 2.14 on page 28
# of Introduction to Python Programming for Business and Social Science Applications
# by Kaefer and Kaefer

# First prompt user to enter trip cost components to string variables
fare = input("Please enter the taxi fare: ")
tip = input("Please enter the tip amount: ")

print("The amounts entered for fare and tip was: ",  
      fare, tip)
print("The data types for each are: ",  
      type(fare), type(tip))

# now add up float values and assign to trip_total variable
trip_total = float(fare)+float(tip)
print ("The total trip cost is: ", "$" + str(trip_total))


#Christopher Early
#11/14/2023
#Use float values to represent the cost to drive the specified distance.

#Get values from user
MPG = float(input("Enter the car's MPG as a decimal number: "))
cost_gallon = float(input("Enter the cost for one gallon of gas: "))

#Calculate cost to drive 20 miles
drive_cost_20 = (20/MPG) * cost_gallon

#Calculate cost to drive 75 miles
drive_cost_75 = (75/MPG) * cost_gallon

#Calculate cost to drive 500 miles
drive_cost_500 = (500/MPG) * cost_gallon

print(drive_cost_20)
print(f"Cost to drive 20 miles is {drive_cost_20:.2f}")

print(drive_cost_75)
print(f"Cost to drive 75 miles is {drive_cost_75:.2f}")

print(drive_cost_500)
print(f"Cost to drive 500 miles is {drive_cost_500:.2f}")

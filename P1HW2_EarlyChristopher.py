print("This program calculates and displays travel expenses")

Initial_Budget = int(input("Enter_Budget:"))
Location = input("Enter_your_travel_destination:")
Fuel = int(input("How much do you think you will spend of gas?"))
Accomodation = int(input("How much will you need for accomodation/hotel?"))
Food = int(input("Last, how much do you need for food?"))

print("------------Travel_Expenses------------")
           
print("Location: ",Location)
print("Initial Budget: ",Initial_Budget)
print("Fuel: ",Fuel)
print("Accomodation",Accomodation)
print("Food", Food)
Remaining_Balance = int(Initial_Budget - Fuel - Accomodation - Food)
print("Remainging Balance",Remaining_Balance)

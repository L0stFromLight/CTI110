#Christopher Early
#11/21/2023
#Use If/Else to determine an employee's pay

#Create variables to hold totals paid to employees
num_em = 0
total_reg = 0
total_ot = 0
total_gross = 0

emp_name = input("Enter employee name or type Done to quit: ")

#Loop to control adding employes
while emp_name != "Done":
    
    num_em += 1
    emp_hours = int(input("Enter employee's hours: "))
    emp_pay = float(input("Enter the employee's pay rate: "))

    #Calculations
    if emp_hours > 40:
        ot_hours = emp_hours - 40
        reg_hours = 40
    #This represents if emp_hours is 40 or less
    else: 
        ot_hours = 0
        reg_hours = emp_hours

    #Calculate pay
    ot_pay = (emp_pay * 1.5) * ot_hours
    total_ot =+ ot_pay

    reg_pay = emp_pay * reg_hours
    total_reg += reg_pay

    gross_pay = ot_pay + reg_pay
    total_gross += gross_pay

    print(f"Employee Name: {emp_name}")
    print(f"Regular Hours: {reg_hours}")
    print(f"OT Hours: {ot_hours}")
    print(f"Regular Pay: {reg_pay}")
    print(f"OT Pay: {ot_pay}")
    print(f"Gross Pay: {gross_pay}")
    print()
    emp_name = input("Enter employee name or type Done to quit:")

#This code executes after loop breaks
print("Done adding employees")
print()
print(f"Total number of employees: {num_em}")
print(f"Total regular pay to emplooyes: {total_reg}")
print(f"Total OT pay to emplooyes: {total_ot}")
print(f"Total gross pay to emplooyes: {total_gross}")

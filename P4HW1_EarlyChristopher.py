#CTI-110
#P4HW1 - Score List
#Christopher Early
#11/20/2023
#

from statistics import mean

num_grades = int(input("How many grades will you enter? "))

#Create a list sto store the grades entered
grades_list = []

#Get grades from user
for i in range(num_grades):
    grade = float(input(f"Enter grade for Module {i + 1}: "))
    while grade < 0 or grade > 100:
        print("You entered an invalid grade: ")
        grade = float(input(f"Enter grade for Module {i + 1}: "))
    grades_list.append(grade)

print (grades_list)

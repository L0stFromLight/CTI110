
#Get input from user
integer = int(input("Enter Integer:"))

#Display output
print(integer)
print("You_entered:",integer)
integer_squared = integer * integer
print(integer,"squared is",integer_squared)
integer_cubed = integer * integer * integer
print("And",integer,"cubed is",integer_cubed,"!!!")

#Get input from user
integer2 = int(input("Enter another integer:"))
integer3 = int(integer + integer2)
integer4 = int(integer * integer2)

#Display output
print(integer,"+", integer2,"is",integer3)
print(integer,"*", integer3, "is", integer4)

#Christopher Early
#11/28/2023
#Use a For loop with the range function

#Get input from user
Num_1 = int(input("Enter a integer: "))
Num_2 = int(input("Enter a integer greater than the first: "))

#If the first number is smaller
if Num_1 < Num_2:
    for i in range (Num_1, Num_2 +1, 5):
        print (i)
else:
#While the input is invalid
    while Num_1 > Num_2 or Num_1 == Num_2:
        print ("The first number must be smaller than the second.")
#Get input from user
        Num_1 = int(input("Enter a integer: "))
        Num_2 = int(input("Enter a integer greater than the first: "))
        for i in range (Num_1, Num_2 +1, 5):
            print (i)

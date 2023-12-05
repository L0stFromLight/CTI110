#Christopher Early
#12/5/2023
#User defined functions

#This function takes
def days_in_feb (is_leap):
    if is_leap == True:
        days = 29
    else:
        days = 28
    return days

def main():
    is_leap_year = False

    input_year = int(input("Enter a year: "))
# inputYear is divisible by 4
    if (input_year % 4) == 0:      
# inputYear is divisible by 100 (century year)
        if (input_year % 100) == 0:  
# inputYear is divisible by 400
            if (input_year % 400) == 0: 
                is_leap_year = True
# inputYear is not divisible by 400
            else:           
                is_leap_year = False
# inputYear is not divisible by 100
        else:             
            is_leap_year = True
# inputYear is not divisible by 4
    else:               
        is_leap_year = False

    #Call our function
    num_days = days_in_feb(is_leap_year)
    print(f"The year {input_year} has {num_days} days in February")

#Call the main function
if __name__ == "__main__":
    main()

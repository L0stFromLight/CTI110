#Christopher Early
#12/7/2023
#Use functions, random numbers and while loops

#Import random library
import random

def show_menu():
    print("Welcome to the Math Quiz")
    print("Main Menu")
    print("------------------------------------------")
    print("1. Adding Random Numbers")
    print("2. Subtracting Randum Numbers")
    print("3. Exit")

#This function adds two random numbers
def add():
    ran1 = random.randint(0,10)
    ran2 = random.randint(0,10)
    print(f"{ran1} + {ran2}")
    return (ran1 + ran2)

def subtract():
    ran1 = random.randint(0,10)
    ran2 = random.randint(0,10)
    print(f"{ran1} - {ran2}")
    return (ran1 - ran2)

#This function simulates the user guessing
#While the guess is wrong, allow the user to guess again

def guessing(guess, correct_answer):
    num_guesses = 0
    while guess != correct_answer:
        num_guesses += 1
        if guess > correct_answer:
            print("Your guess is too high")
            guess = int(input("Guess again? "))
        else:
            print("Your guess is too low")
            guess = int(input("Guess again? "))   

    #User answer is correct, the while loop breaks
    print("Your answer is correct.")
    print(f"It took you {num_guesses} incorrect guesses to get it right.")

#Main Function
def main():
    show_menu()
    user_option = int(input("Please choose a menu option: "))
    while user_option != 3:
        if user_option == 1:
            ran_sum = add()
            my_guess = int(input("What is your guess? "))
            guessing(my_guess, ran_sum)
            print()
            show_menu()
            user_option = int(input("Please choose one of the menu options: "))

        if user_option == 2:
            ran_sum = add()
            my_guess = int(input("What is your guess? "))
            guessing(my_guess, ran_sum)
            print()
            show_menu()
            user_option = int(input("Please choose one of the menu options: "))
print("Thank you for playing, goodbye!")
                            
#Call the main function
if __name__ == "__main__":
    main()

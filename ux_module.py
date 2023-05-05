import sys
def opening_statement():
    print('Welcome to the Room Booking System')
    input_invalid = 0
    while (input_invalid):
        user_input = input("Press 'b' to book a room or 'q' to quit:")
        if user_input == 'b':
            input_invalid = 1
            show_locations()
        elif user_input == 'q':
            input_invalid = 1
            sys.exit()
        else: 
            print("Please enter a valid character.")

def show_locations():
    input_invalid = 0
    while (input_invalid):
        print("Enter a location of your choice: ")
        user_input = input("1) IV Learning Centre\n2) Library of Arts\n3) WD Library")
        if user_input == '1' or user_input == '2' or user_input == '3':
            input_invalid = 1
            check_availability(user_input)
        else: 
            print("Please enter a valid character.")
    
def check_availability():
    
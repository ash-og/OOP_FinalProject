import LMS_Classes
import objectCreation
import os


def browseCatalogue():
    print("ID \t-\t Title \t\t-\t\t Author")
    for value in book_obj_dict.values():
        print(value)


def staff_menu():
    """Menu for staff users"""
    while True:
        user_input = input("What would you like to do?\n"
                           "1. Modify Member\n"
                           "2. Modify Library\n"
                           "3. Modify Catalogue Item\n"
                           "4. Change Item State\n"
                           "5. Return to Main Menu\n"
                           "6. Quit Program \n")
        if user_input == "1":
            pass
            input("Press any key to continue..\n")
        elif user_input == "2":
            pass
            input("Press any key to continue..\n")
        elif user_input == "3":
            print("Quitting program...")
            break
        else:
            print("Not a valid option. Try again.\n")

def member_menu():
    """Menu for Member users"""
    while True:
        user_input = input("What would you like to do?\n"
                           "1. Browse Catalogue\n"
                           "2. Borrow Catalogue Item\n"
                           "4. Return Catalogue Item\n"
                           "2. Join Library\n"
                           "3. Cancel Membership\n"
                           "5. Return to Main Menu\n"
                           "6. Quit Program \n")
        if user_input == "1":
            pass
            input("Press any key to continue..\n")
        elif user_input == "2":
            pass
            input("Press any key to continue..\n")
        elif user_input == "3":
            print("Quitting program...")
            break
        else:
            print("Not a valid option. Try again.\n")


def mainMenu():
     while True:
        user_input = input("Which user are you?\n"
                           "1. Staff\n"
                           "2. Member\n"
                           "3. Quit Program\n")
        if user_input == "1":
            staff_menu()
            input("Press any key to continue..\n")
        elif user_input == "2":
            member_menu()
            input("Press any key to continue..\n")
        elif user_input == "3":
            print("Quitting program...")
            break
        else:
            print("Not a valid option. Try again.\n")

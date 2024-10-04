print("----") # line separator. This is an example of an inline comment.

"""
This is the application menu telling the user what
valid options are available to be selected.
This is an example of a comment block.
"""

# Function to display the main menu
def main_menu():
    print()
    # Welcome message
    print("\t\t**** Welcome to the Dashboard ****")
    print("\t\t*** ENTER A MENU CHOICE NUMBER ***")
    print()
    # Options for the user to choose from
    print('99) Exit the program')
    # return the user's choice
    choice = int(input("\n  Enter a menu number: "))
    return choice

"""
The execution of all the code is modularised with separate functions.
The menu option function will be called in the menu code at the end of this file
to carry out the selected tasks.
"""



"""
This is the application's menu implementation. It is called
right at the top of this file, and runs when the program launches.
It is set up to run until the user enters 99 to exit the structure.
"""
# *****************************************************************
# *****************************************************************
# MENU Implementation
# *****************************************************************
# Display menu when application launches
x = main_menu()
"""
The while loop is used to allow the user to use more than
one feature until they exit. The break intruction closes
the program.
"""
while x == 99:
    break

    x = main_menu()

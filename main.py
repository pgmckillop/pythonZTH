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
    print('1) Beginner: Hello basic')
    print('2) Beginner: Numbers Basic')
    print('3) Intermediate: Numbers Value Check')
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
Menu Option 1. Beginner: Hello basic.
When we start working with a new computer programming language, we conventionally
create a Hello World script. It might seem trivial, but it's a very good test
that the Input and Output features of the language are working.
"""


def menu_option_1():
    forename = input("Enter your first name: ")
    print("Hello", forename)

"""
Menu Option 2. Beginner: Numbers basic.
Programming with a Sequence structure. 
There is no conditional branching, and each
instruction is carried out once only.
"""


def menu_option_2():
    # set up an empty list to store the numbers entered
    numbers_entered = []
    print("You are going to be asked to enter 3 integer numbers. Enter them at the prompt.")
    print(" ")
    num1 = int(input("Enter the first number: "))
    numbers_entered.append(num1)
    num2 = int(input("Enter the second number: "))
    numbers_entered.append(num2)
    num3 = int(input("Enter the third number: "))
    numbers_entered.append(num3)
    print(" ")
    print("The numbers you entered are: ", numbers_entered)

"""
-- INDEPENDENT EXTENSION TASK
-- Menu option 2 Extension Task
--
Develop the function further to print out a 
total of the numbers entered.
"""

"""
Menu Option 3. Intermediate: Numbers Value Check.
There is use of condition branching with if .. else structures.
The use of try: .. except: is an example of error handling.
The check for integer values is carried out by he try: to cast to int(). If it fails,
the value is not an integer. This will catch numbers with a decimal value, and numbers
entered as a word.
The menu option function uses Iteration.
"""


def is_integer(value):
    try:
        int(value)
        return True
    except ValueError:
        print("That\'s not an integer value.")
        print("")
        return False


def menu_option_3():
    # set up an empty list to store the numbers entered
    numbers_entered = []
    print("You are going to be asked to enter 3 integer numbers. Enter them at the prompt.")
    print(" ")
    num1 = input("Enter the first number: ")
    while is_integer(num1) == False:
        print("Please enter an integer value")
        num1 = input("Enter the first number: ")
    numbers_entered.append(num1)
    num2 = input("Enter the second number: ")
    while is_integer(num2) == False:
        print("Please enter an integer value")
        num2 = input("Enter the second number: ")
    numbers_entered.append(num2)
    num3 = input("Enter the third number: ")
    while is_integer(num3) == False:
        print("Please enter an integer value")
        num3 = input("Enter the third number: ")
    numbers_entered.append(num3)
    print(" ")
    print("The numbers you entered are: ", numbers_entered)


"""
-- INDEPENDENT EXTENSION TASK
-- Menu option 3 Extension Task
--
Develop the function further to print out 
the numbers entered in ascending order.
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

while x == 1 or x == 2 or x == 3 or x == 99:
    if x == 1:
        print(" ")
        print("You have selected the Beginner: Hello basic")
        # print("Hello World!")
        menu_option_1()
    elif x == 2:
        print("You have selected the Beginner: Numbers Basic")
        menu_option_2()
    elif x == 3:
        print(" ")
        print("You have selected the Intermediate: Numbers Value Check")
        menu_option_3()
    elif x == 99:
        print(" ")
        print("You have selected to Exit the program")
        break

    x = main_menu()

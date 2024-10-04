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
    print('4) Intermediate: Numbers Range Check')
    print('5) Intermediate: Average of 3 Numbers')
    print('6) Intermediate: Highest Entered Number')
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
Menu Option 4. Intermediate: Numbers range check
This is an example of decomposition and modularisation. Each of the
functions is called by other functions. This makes code testing and maintenance 
easier. 
There is use of condition branching with if .. else structures.
The use of try: .. except: is an example of error handling. If we 'catch' the 
exception, we can deal with it in code to avoid the program crashing.
"""


# First check if the number is less than 20
def is_valid(num):
    """Check if the number is less than 20."""
    return num < 20


# Combined function to check if the input is an integer and less than 12
def is_integer_and_valid(user_input):
    try:
        # Attempt to convert the input to an integer
        converted_number = int(user_input)
        # Check if the converted number is less than 12
        if is_valid(converted_number):
            return True  # Return True if the number is also less than 12
        else:
            print("The number must be less than 20, try again")
            return False  # Return False if the number is 12 or greater
    except ValueError:
        # A ValueError occurs if the conversion fails
        print("The number entered is not an integer, try again")
        return False  # Return False if the input is not an integer


# Bringing it together in the menu option
def menu_option_4():
    # set up an empty list to store the numbers entered
    numbers_entered = []
    print("You are going to be asked to enter 3 integer numbers. Enter them at the prompt.")
    print("Each number must be less than 20")
    print(" ")
    num1 = input("Enter the first number: ")
    while not is_integer_and_valid(num1):
        print("Please enter an integer value")
        num1 = input("Enter the first number: ")
    numbers_entered.append(num1)
    num2 = input("Enter the second number: ")
    while not is_integer_and_valid(num2):
        print("Please enter an integer value")
        num2 = input("Enter the second number: ")
    numbers_entered.append(num2)
    num3 = input("Enter the third number: ")
    while not is_integer_and_valid(num3):
        print("Please enter an integer value")
        num3 = input("Enter the third number: ")
    numbers_entered.append(num3)
    print(" ")
    print("The numbers you entered are: ", numbers_entered)

"""
-- INDEPENDENT EXTENSION TASK
-- Menu option 4 Extension Task
--
Develop the function further to check that
the number entered is between a lower AND upper value.
"""
"""
Menu Option 5. Intermediate: Average of 3 Numbers
The numbers_total variable is a tracking variable that will
be an updated total with each number entered by the user.
"""


# We can reuse the functions we created for menu-option-4
def menu_option_5():
    # set up an empty list to store the numbers entered
    numbers_entered = []
    # set up a variable to store the total of the numbers entered
    numbers_total = 0

    print("You are going to be asked to enter 3 integer numbers. Enter them at the prompt.")
    print("Each number must be less than 20")
    print(" ")
    num1 = input("Enter the first number: ")
    while not is_integer_and_valid(num1):
        print("Please enter an integer value")
        num1 = input("Enter the first number: ")
    numbers_entered.append(num1)
    numbers_total += int(num1)
    num2 = input("Enter the second number: ")
    while not is_integer_and_valid(num2):
        print("Please enter an integer value")
        num2 = input("Enter the second number: ")
    numbers_entered.append(num2)
    numbers_total += int(num2)
    num3 = input("Enter the third number: ")
    while not is_integer_and_valid(num3):
        print("Please enter an integer value")
        num3 = input("Enter the third number: ")
    numbers_entered.append(num3)
    numbers_total += int(num3)
    print(" ")
    print("The numbers you entered are: ", numbers_entered)
    print("The average of the numbers entered is: ", numbers_total / 3)
    # print("The average of the numbers entered is: ", sum(numbers_entered) / len(numbers_entered))


"""
-- INDEPENDENT EXTENSION TASK
-- Menu option 5 Extension Task
--
Develop the function further to only
permit a maximum of 3 numbers to be entered.
"""

"""
Menu_option_6 - Intermediate: Highest number entered
Note: We could have used a tracking variable to record the current highest value
as the user enters ach number, 
but Python has a useful max() method that can be used with an array structure.
"""


def menu_option_6():
    # set up an empty list to store the numbers entered
    numbers_entered = []
    print("You are going to be asked to enter 3 integer numbers. Enter them at the prompt.")
    print(" ")
    num1 = input("Enter the first number: ")
    while not is_integer_and_valid(num1):
        print("Please enter an integer value")
        num1 = input("Enter the first number: ")
    numbers_entered.append(num1)
    num2 = input("Enter the second number: ")
    while not is_integer_and_valid(num2):
        print("Please enter an integer value")
        num2 = input("Enter the second number: ")
    numbers_entered.append(num2)
    num3 = input("Enter the third number: ")
    while not is_integer_and_valid(num3):
        print("Please enter an integer value")
        num3 = input("Enter the third number: ")
    numbers_entered.append(num3)
    print(" ")
    print("The numbers you entered are: ", numbers_entered)
    # We can use a built-in method that works for Python lists to find the highest number
    print("The highest number entered is: ", max(numbers_entered))
    #
    # this code has a bug. Can you resolve it?
    #

"""
-- INDEPENDENT EXTENSION TASK
-- Menu option 6 Extension Task
--
Change the way the function works to return
the lowest number entered using a for iteration loop.
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

while x == 1 or x == 2 or x == 3 or x == 4 or x == 5 or x == 6 or x == 99:
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
    elif x == 4:
        print(" ")
        print("You have selected the Intermediate: Numbers Range Check")
        menu_option_4()
    elif x == 5:
        print(" ")
        print("You have selected the Intermediate: Average of 3 Numbers")
        menu_option_5()
    elif x == 6:
        print(" ")
        print("You have selected the Intermediate: Highest number entered")
        menu_option_6()
    elif x == 99:
        print(" ")
        print("You have selected to Exit the program")
        break

    x = main_menu()

# Emmanuel Cruz 

# Nov 12, 2024

# The program prompts the user to enter two values and then checks and prints whether the values are equal or not.

def are_values_equal():
    # Get input from the user
    value1 = input("Please enter the first value: ")
    value2 = input("Please enter the second value: ")

    # Compare the two values
    if value1 == value2:
        print("The values are equal.")
    else:
        print("The values are not equal.")

# Call the function
are_values_equal()


# Emmanuel Cruz 

# Nov 12, 2024

# The program prompts the user to enter two values, calculates their sum, and prints whether the sum is greater than, less than, or equal to 10. 

def less_equal_greater():
    value1 = input("Add the first value: ")
    value2 = input("Add the second value: ")
    # Convert values to integers or floats for summation
    try:
        num1 = float(value1)
        num2 = float(value2)
    except ValueError:
        print("Please enter valid numbers.")
        return

    # Calculate the sum of the first two values
    sum_of_values = num1 + num2
    
    # Determine if the sum is greater than, less than, or equal to 10
    if sum_of_values > 10:
        print(f"The sum of {num1} and {num2} is greater than 10.")
    elif sum_of_values < 10:
        print(f"The sum of {num1} and {num2} is less than 10.")
    else:
        print(f"The sum of {num1} and {num2} is equal to 10.")

# Call the function
less_equal_greater()


# Emmanuel Cruz 

# Nov 12, 2024

# 

def check_five_in_list(input_list):
    # Check if 5 is in the provided list
    if 5 in input_list:
        print("The value of 5 is in the list")
    else:
        print("The value of 5 is not in the list")


# Example for code
example_list = [1,2,3,4,5,7,8,9,10]
check_five_in_list(example_list)



#write a function
import resources

def view_item(number):
    print(f"{resources.Emmanuel.weapons}")
    #print out the lisy connected to the task number 
    #if the number is 1, print out [ "rope, coat, and first aid kit"]
    #if the number is 2, print out ["pan, groceries"]
    #if the number is 3, print out ["pen, paper, idea"]

    if number == 1:
        print(['rope'], ['coat'], ['first aid kit'])
        # for every item on the list that i need, i want to see if it is in my weapons
        for item in ['rope','coat','first aid kit']:
            if item not in resources.Emmanuel.weapons:
                print(f"Hey, you don't have {item}")
                return False
            print("You have evrything you need, good luck!")
            return True
    elif number == 2:
        print(['pan'],['groceries'])
    elif number == 3:
        print(['pen'], ['paper'], ['idea'])



view_item(1)

    #see printed out: ["pan, groceries"]
# whether your game character has picked up all the items needed to perform certain tasks and checks against any weaknesses.Confirm checks with print statements. The function will take a number in as an argument. You can match the number to the task below. You don’t have to plan for inputs outside of [1,2,3].

# how do i look in my characters 
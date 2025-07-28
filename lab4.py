# Set up a control variable (e.g., continue_checking = "yes")

# Use a while loop that checks if continue_checking is "yes"https://docs.google.com/forms/u/0/d/e/1FAIpQLSd0d6aJHVtJqTxv0H7PfF-rYhupFYWjddnOTJCbIrOyttCAcA/viewform?usp=form_confirm&edit2=2_ABaOnuetj6RIGnTDfL1N9L6h52eSZ-UcMZ0H4LF0Z87y1mpKDdDiI3W1RIocpkh55A
# Inside the loop:
    # Ask the user for an age
    # Check if they are eligible to vote (if age >= 18)
	# if they are, what should we display
	# if they aren’t, what should we display
    # Ask if user wants to check another age (i.e., update continue_checking)


continue_checking = "yes"

while continue_checking == "yes":
    check_age = input("Enter a number: ")
    check_age = int(check_age)
    
    if check_age >= 18:
        print("This person is eligible to vote")
    
    if check_age < 18:
        print("This person is not eligible to vote")

    continue_check = input("Want to check another age? Enter 1 for YES, Enter 2 for NO: ")
    if int(continue_check) == 1: 
        continue
    else:
        continue_checking = "no"


# Define a list of numbers (e.g., numbers = [15, -7, 0, 23, -42, 8])

# Use a for loop to iterate over each number in the list
    # Inside the loop, check if the number is positive, negative, or zero
	# if the number is positive, what should we display?
	# if the number is negative, what should we display?
	# if the number is neither, what should we display?

numbers = [14, 0, 4, -7, 16, -3, 18, 97, 102, -31]
for number in numbers:
    
    # we need to tell the computer whether the number is less than or greater than 0 
    if number > 0:
        print("The number is positive")
    if number < 0:
        print("The number is negative.")
    if number == 0:
        print("The number is neither")
        

    print(number)

'''
 5 different kinds of blocks: “coal”, “dirt”, “diamond”, “gravel”, and “stone”. 

You can use either a for or while loop for this question. Be creative! Here’s some helpful documentation for len() and range() if you find them useful.
'''
# Create a program to loop through your inventory that 1) prints out what block you found and 2) if it’s a “diamond”, prints out “Jackpot!”. 

# lets first put the five kinds of blocks in a list
blocks = ["coal", "dirt", "diamond", "gravel", "stone"] 

# use either a for or while loop to iterate over each block, using for loop seems easier
for block in blocks:
    # print all the blocks and if its a diamond, also print jackpot
    print(block)

    if "diamond" == block:
        print("jackpot")






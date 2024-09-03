my_string = "LaunchCode"


# a) Use string methods to remove the first three characters from the string and add them to the end.
altered_string = my_string[3:] + my_string[0:3]


# Use a template literal to print the original and modified string in a descriptive phrase.
print('We are changing', my_string, 'into', altered_string + '.')


# b) Modify your code to accept user input. Query the user to enter the number of letters that will be relocated.
# user_selection = input('Please select a number:')
# user_selection_int = int(user_selection)
# new_altered_string = my_string[user_selection_int:] + my_string[0:user_selection_int]
# print(new_altered_string)

# c) Add validation to your code to deal with user inputs that are longer than the word. In such cases, default to moving 3 characters. Also, the template literal should note the error.
user_selection = input('Please select a number:')
user_selection_int = int(user_selection)
new_altered_string = my_string[user_selection_int:] + my_string[0:user_selection_int]

if user_selection_int > 9:
    print('Your number is too big.', 'Here is the default answer:', altered_string)

else:  
    print(new_altered_string)
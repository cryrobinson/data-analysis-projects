food = "water bottles,meal packs,snacks,chocolate"
equipment = "space suits,jet packs,tool belts,thermal detonators"
pets = "parrots,cats,moose,alien eggs"
sleep_aids = "blankets,pillows,eyepatches,alarm clocks"

# a) Use split to convert the strings into four cabinet lists. Alphabetize the contents of each cabinet.
food_list = food.split(',')
equipment_list = equipment.split(',')
pets_list = pets.split(',')
sleep_aids_list = sleep_aids.split(',')

food_list.sort()
equipment_list.sort()
pets_list.sort()
sleep_aids_list.sort()

print("Food Cabinet:", food_list)
print("Equipment Cabinet:", equipment_list)
print("Pets Cabinet:", pets_list)
print("Sleep Aids Cabinet:", sleep_aids_list)
# b) Initialize a cargo_hold list and add the cabinet lists to it. Print cargo_hold to verify its structure.
cargo_hold = [food_list, equipment_list, pets_list, sleep_aids_list]

print("Cargo Hold:", cargo_hold)
# c) Query the user to select a cabinet (0 - 3) in the cargo_hold.
selection = input("Enter the number of the cabinet you want: ")

if selection == "0" or selection == "1" or selection == "2" or selection == "3":
    selection = int(selection)
    selected_cabinet = cargo_hold[selection]
    print("You selected: " + str(selected_cabinet))
else:
    print("Invalid selection. Please choose a number between 0 and 3.")


# d) Use bracket notation and format to display the contents of the selected cabinet. If the user entered an invalid number, print an error message.



# e) Modify the code to query the user for BOTH a cabinet in cargo_hold AND a particular item. Use the in method to check if the cabinet contains the selected item, then print “Cabinet ____ DOES/DOES NOT contain ____.”
if selection in ["0", "1", "2", "3"]:
    selection = int(selection)
    selected_cabinet = cargo_hold[selection]

    item = input("Enter the item you want to check: ")

    if item in selected_cabinet:
        print("Cabinet {} DOES contain '{}'.".format(selection, item))
    else:
        print("Cabinet {} DOES NOT contain '{}'.".format(selection, item))
else:
    print("Error: Invalid selection. Please choose a number between 0 and 3.")
# Welcome to my pizza calculator  program
# Alex Stomberg
 # Period 7
 # 10/10/2018
 #size_6, size_10,size_14, size_16, toppings_6, toppings_10,toppings_14, toppings_16
 #toppings_6,toppings_10, toppings_14,toppings_16, extra_610, extra_1416
 #amount_topping, size, extra_toppings

#This is the print statments that welcomes my program
print ("Welcome to my pizza calculations Program!\n\n")

#This just prints out the menu
print ("Size:")
print ("6  inch .............$4.00")
print ("10 inch .............$7.50")
print ("14 inch .............$12.90")
print ("16 inch .............$14.25\n\n")

print ("Cost of Toppings:")
print ("6  inch .............$0.50")
print ("10 inch .............$0.6")
print ("14 inch .............$0.75")
print ("16 inch .............$0.90\n\n")

print ("Extra Cheese")
print ("6, 10 inch ............$1")
print ("14, 16 inch ...........$2\n\n")


print ("Welcome to Deanna’s Pizza Parlor\n\n")
print ("1........6 inch")
print ("2.......10 inch")
print ("3.......14 inch")
print ("4.......16 inch\n")

#varibles that list the cost of the menu
size_6= 4.00
size_10=7.50
size_14=12.90
size_16=14.25

toppings_6=0.50
toppings_10=0.6
toppings_14=0.75
toppings_16=0.90

extra_610=1
extra_1416=2

#int-input and input varibles that ask the user about the items he wants to choose
size = int(input("Enter the number (1 – 4) corresponding to the pizza size:"))
amount_toppings = int(input("Enter the number of toppings: "))
extra_toppings = input("Extra cheese (y or n)?")

#if statement that says if the user chooses size: 1 and one for everything else
# including cheese it will calculate the price
if size == 1 and amount_toppings  == 1 and extra_toppings == 'y':
    print ("\nYour total for your pizza is ${0:.2f}".format(size_6+toppings_6+extra_610*0.06),"\nThank you!")

#elif statments that will calculate the other costs for each item with
# cheese or without also every size and topping
elif size == 1 and amount_toppings  == 1 and extra_toppings == 'n':
    print ("\nYour total for your pizza is ${0:.2f}".format(size_6+toppings_6*0.06),"\nThank you!")

elif size == 1 and amount_toppings  == 1 and extra_toppings == 'y':
    print ("\nYour total for your pizza is ${0:.2f}".format(size_6+toppings_6+extra_610*0.06),"\nThank you!")

elif size == 1 and amount_toppings  == 2 and extra_toppings == 'n':
    print ("\nYour total for your pizza is ${0:.2f}".format(size_6+toppings_10*0.06),"\nThank you!")

elif size == 1 and amount_toppings == 2 and extra_toppings == 'y':
    print ("\nYour total for your pizza is ${0:.2f}".format(size_6+toppings_10+extra_610*0.06),"\nThank you!")

elif size == 1 and amount_toppings  == 3 and extra_toppings == 'n':
    print ("\nYour total for your pizza is ${0:.2f}".format(size_6+toppings_14*0.06),"\nThank you!")

elif size == 1 and amount_toppings == 3 and extra_toppings == 'y':
    print ("\nYour total for your pizza is ${0:.2f}".format(size_6+toppings_14+extra_610*0.06),"\nThank you!")

elif size == 1 and amount_toppings  == 4 and extra_toppings == 'n':
    print ("\nYour total for your pizza is ${0:.2f}".format(size_6+toppings_16*0.06),"\nThank you!")

elif size == 1 and amount_toppings == 4 and extra_toppings == 'y':
    print ("\nYour total for your pizza is ${0:.2f}".format(size_6+toppings_16+extra_610*0.06),"\nThank you!")

elif size == 1 and amount_toppings  == 4 and extra_toppings == 'n':
    print ("\nYour total for your pizza is ${0:.2f}".format(size_6+toppings_16*0.06),"\nThank you!")

elif size == 1 and amount_toppings == 4 and extra_toppings == 'y':
    print ("\nYour total for your pizza is ${0:.2f}".format(size_6+toppings_16+extra_610*0.06),"\nThank you!")

elif size == 2 and amount_toppings  == 2 and extra_toppings == 'y':
    print ("\nYour total for your pizza is ${0:.2f}".format(size_10+toppings_10+extra_610*0.06),"\nThank you!")

elif size == 2 and amount_toppings  == 2 and extra_toppings == 'n':
    print("\nYour total for your pizza is ${0:.2f}".format(size_10 + toppings_10* 0.06), "\nThank you!")

elif size == 2 and amount_toppings  == 1 and extra_toppings == 'y':
    print ("\nYour total for your pizza is ${0:.2f}".format(size_10+toppings_6+extra_610*0.06),"\nThank you!")

elif size == 2 and amount_toppings  == 1 and extra_toppings == 'n':
    print("\nYour total for your pizza is ${0:.2f}".format(size_10 + toppings_6* 0.06), "\nThank you!")

elif size == 2 and amount_toppings  == 3 and extra_toppings == 'y':
    print ("\nYour total for your pizza is ${0:.2f}".format(size_10+toppings_14+extra_610*0.06),"\nThank you!")

elif size == 2 and amount_toppings  == 3 and extra_toppings == 'n':
    print("\nYour total for your pizza is ${0:.2f}".format(size_10 + toppings_14 * 0.06), "\nThank you!")

elif size == 2 and amount_toppings  == 4 and extra_toppings == 'y':
    print ("\nYour total for your pizza is ${0:.2f}".format(size_10+toppings_16+extra_610*0.06),"\nThank you!")

elif size == 2 and amount_toppings  == 4 and extra_toppings == 'n':
    print("\nYour total for your pizza is ${0:.2f}".format(size_10 + toppings_16 * 0.06), "\nThank you!")

elif size == 3 and amount_toppings  == 3 and extra_toppings == 'y':
    print("\nYour total for your pizza is ${0:.2f}".format(size_14 + toppings_14+extra_1416* 0.06), "\nThank you!")

elif size == 3 and amount_toppings  == 3 and extra_toppings == 'n':
    print("\nYour total for your pizza is ${0:.2f}".format(size_14 + toppings_14 * 0.06), "\nThank you!")

elif size == 3 and amount_toppings  == 1 and extra_toppings == 'y':
    print("\nYour total for your pizza is ${0:.2f}".format(size_14 + toppings_6+extra_1416* 0.06), "\nThank you!")

elif size == 3 and amount_toppings  == 1 and extra_toppings == 'n':
    print("\nYour total for your pizza is ${0:.2f}".format(size_14 + toppings_6 * 0.06), "\nThank you!")

elif size == 3 and amount_toppings  == 2 and extra_toppings == 'y':
    print("\nYour total for your pizza is ${0:.2f}".format(size_14 + toppings_10+extra_1416* 0.06), "\nThank you!")

elif size == 3 and amount_toppings  == 2 and extra_toppings == 'n':
    print("\nYour total for your pizza is ${0:.2f}".format(size_14 + toppings_10 * 0.06), "\nThank you!")

elif size == 3 and amount_toppings  == 4 and extra_toppings == 'y':
    print("\nYour total for your pizza is ${0:.2f}".format(size_14 + toppings_16+extra_1416* 0.06), "\nThank you!")

elif size == 3 and amount_toppings  == 4 and extra_toppings == 'n':
    print("\nYour total for your pizza is ${0:.2f}".format(size_14 + toppings_16 * 0.06), "\nThank you!")

elif size == 4 and amount_toppings  == 4 and extra_toppings == 'y' :
    print("\nYour total for your pizza is ${0:.2f}".format(size_16 + toppings_16+extra_1416* 0.06), "\nThank you!")

elif size == 4 and amount_toppings  == 4 and extra_toppings == 'n':
    print("\nYour total for your pizza is ${0:.2f}".format(size_16 + toppings_16* 0.06), "\nThank you!")

elif size == 4 and amount_toppings  == 3 and extra_toppings == 'y' :
    print("\nYour total for your pizza is ${0:.2f}".format(size_16 + toppings_14+extra_1416* 0.06), "\nThank you!")

elif size == 4 and amount_toppings  == 3 and extra_toppings == 'n':
    print("\nYour total for your pizza is ${0:.2f}".format(size_16 + toppings_14* 0.06), "\nThank you!")

elif size == 4 and amount_toppings  == 2 and extra_toppings == 'y' :
    print("\nYour total for your pizza is ${0:.2f}".format(size_16 + toppings_10+extra_1416* 0.06), "\nThank you!")

elif size == 4 and amount_toppings  == 2 and extra_toppings == 'n':
    print("\nYour total for your pizza is ${0:.2f}".format(size_16 + toppings_10* 0.06), "\nThank you!")

elif size == 4 and amount_toppings  == 1 and extra_toppings == 'y' :
    print("\nYour total for your pizza is ${0:.2f}".format(size_16 + toppings_16+extra_1416* 0.06), "\nThank you!")

elif size == 4 and amount_toppings  == 1 and extra_toppings == 'n':
    print("\nYour total for your pizza is ${0:.2f}".format(size_16 + toppings_16* 0.06), "\nThank you!")
#if the user enters a choice less than 1 it will tell him to run the program again
elif size < 1  and amount_toppings < 1:
    print("You have entered an invalid choice. Please run this program again.")

#if the user enters a choice greater than 4 it will tell him to run the program again
elif size > 4  and amount_toppings > 4:
    print("You have entered an invalid choice. Please run this program again
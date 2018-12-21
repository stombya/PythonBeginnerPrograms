#Alex Stomberg
#12/12/18
#Peiod 7, Python Programming
#def welcome() is the welcome message function, def inputs() contains all the inputs from the user. The number questions are in a float. def calculations(p2,r2,n2,y2) contains the equation. def display () outputs the table row with the user inputs and the final compound value. the main() function contains the while loop and defines each local varible in all the other functions.

#welcome message function
def welcome():
  print("welcome to the compound intrest program")

#function for all the inputs
def inputs():
  name=input("\nWhat's your Name? ")
  p = float(input("Amount to be invested? "))
  r = float(input("Annual rate of interest? (type without percent) "))
  n = float(input("Number of times compounded per year? "))
  y = float(input("Number of years investment will be made "))
  return name, p, r, n, y

#function for the calculations
def calculations(p2,r2,n2,y2):
  final = p2 * (((1 + ((r2/100.0)/n2)) ** (n2*y2)))
  return final
#function for the display. outputs the compound value from the calculations()
def display(name,p2,r2,n2,y2,final):
    print("\nName ",name)
    print("Principle ",p2)
    print("Rate ",r2,"%")
    print("# times Compound ",n2,"Days")
    print("Length of Investment ",y2,"years")
    print ("Final Worth ",str(round(final,2)),"$")
#function that defines each value in all the other function
def main():
  welcome()
  repeat = True
# while that runs until the user wishes to exit
  while repeat:
    name, p, r, n, y = inputs()
    final = calculations(p, r, n, y)
    display(name,p, r, n, y, final)
# prompt and read if the user wishes to continue
    choice = input("\nWould you like to run the program again (y or n)? ")
# set repeat to False to exit the loop, if the user enters n
    if choice == 'n' or choice == 'N':
      repeat = False
      print()
      print("Thank you...")
main()


input("\n\nPress the enter key to exit.")

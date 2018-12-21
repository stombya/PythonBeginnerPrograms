# Welcome to my Celestial program
# Alex Stomberg
 # Period 7 #
 # 10/5/2018
 # weight, venus,moon,jupiter,choice

print ("Welcome to the celsetial program!\n")


weight = int(input("What is your earth weight:"))



print ("\n1.venus")
print ("2.moon")
print ("3.mars")
print ("4.jupiter")


choice = int(input("Choose your Planet:"))

venus = 0.91
moon = 0.17
mars = 0.38
jupiter = 2.54

print ("Planet\t\tPlanet Weight")
if choice == 1:
  print ("Venus\t\t",weight*venus)
elif choice == 2:
  print ("Moon\t\t",weight*moon)
elif choice == 3:
  print ("Mars\t\t",weight*mars)
elif choice == 4:
  print ("Jupiter\t\t",weight*jupiter)
else:
    print ("\nYou've entered an invalid option" "please run the program again")
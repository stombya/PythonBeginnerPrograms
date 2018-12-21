#Alex Stomberg
#program that has student class data about gpa,grade, and names. You will be able to analyze that data. 
# Alex Stomberg
# Period 7
# 11/30/2018
#dictionary that containts the key(grandpa),value(son,dad)
#pygiflet print out the ascii art.The menu varible is just the print for all the choices.def ascending_sort_by_last_name(l) is the function that creates out sorted list for ascending gpa. The print_students_descending_gpa(l) is the function that creates a sort for the descending gpa sort. def sort() sorts the list without gpa. students is the list, ans is the question input, for loop for last_name, first_name, c, gen,gpa in students seperates out each item in the list.
import pyfiglet
menu=("""
  1.   School List
  2.   Sophomores
  3.   Juniors
  4.   Above Average Students
  5.   Alphabetical List
  6.   Highest and Lowest GPA
  7.   Find Student
  8.   Exit (Loop the menu – Extra Credit)
  """)
print("")
#Credits to Peter Waller for this ASCII art and pyfiglet
#prints ascii art
result = pyfiglet.figlet_format("Student info analyzer Program", font = "digital")
print(result)
print(menu)

#function that creates out sorted list for ascending gpa
def ascending_sort_by_last_name(l):
    sorted_list=list(sorted(l,key=lambda row:row[1]))
    #relabels the row
    print('{0:<15}{1:<15}{2:<6}{3:>5}'.format('First Name','Last Name','Year','GPA'))
    for row in sorted_list:
        print('{0:<15}{1:<15}{2:<6}{3:>5}'.format(row[0],row[1],row[2],row[4]))

#function that creates a sort for the descending gpa sort
def print_students_descending_gpa(l):
    sorted_list = list(sorted(l, key=lambda row: row[4],reverse=True))
    print('{0:<15}{1:<15}{2:<6}{3:>5}'.format('First Name', 'Last Name', 'Year', 'GPA'))
    for row in sorted_list:
        print('{0:<15}{1:<15}{2:<6}{3:>5}'.format(row[0], row[1], row[2], row[4]))
#function that creates a sort without the gpa
def sort(l):
    sorted_list = list(sorted(l, key=lambda row: row[4],reverse=True))
    print('{0:<15}{1:<15}{2:<6}'.format('First Name', 'Last Name', 'Year'))
    for row in sorted_list:
        print('{0:<15}{1:<15}{2:<6}'.format(row[0], row[1], row[2]))

# list of student data
students = [("White", "Snow", 9, "F", 3.56), ("Sprat", "Jack", 12, "M", 2.0), ("Contrary", "Mary", 9, "F", 3.674),
                ("Dumpty", "Humpty", 11, "M", 2.342), ("Bunny", "Easter", 10, "M", 4.233),
                ("Wonderland", "Alice", 10, "F", 3.755), ("Bunyon", "Paul", 11, "M", 1.434),
                ("Penny", "Henny", 9, "F", 2.54), ("Hatter", "Mad", 11, "M", 4.522), ("Munk", "Chip", 10, "M", 3.0),
                ("Hood", "Red Riding", 10, "F", 3.137), ("Bunny", "Bugs", 11, "M", 2.12),
                ("Duck", "Daffy", 11, "M", 3.564), ("Ant", "Atom", 12, "M", 3.333), ("Mouse", "Mickey", 10, "M", 3.975),
                ("Brown", "Charlie", 9, "M", 1.25)]

#Gpa list
gpa_grade=[3.56,2.0,3.674,2.342,4.233, 3.755,1.434,2.54,4.522,3.0,3.137,2.12,3.564,3.333,3.975,1.25]

ans=input("What would you like to do?")
#Print first name, last name, year  /   print # of freshman, sophomores, juniors, seniors)
if ans=="1":
  sort(students)
  #sum(x.count) is a way of counting inside a nested sequence for a specific value
  print("There are",sum(x.count(9) for x in students),"Freshman,",sum(x.count(10) for x in students),"Sophmore,",sum(x.count(11) for x in students),"Junior, and",sum(x.count(12) for x in students),"Senior Students")
#Print Sophomores  /  first name, last name  /  print number of males and females 
elif ans=="2":
 print("There are",sum(x.count("M") for x in students),"Male Students and",sum(x.count("F") for x in students),"Female Students")
 for last_name, first_name, c, gen,gpa in students:
      if c == 9:
        print("Sophmores")
        print(first_name,last_name)
        continue
#Print Juniors  /  first name, last name /   print number of males and females
elif ans=="3":
  print("There are",sum(x.count("M") for x in students),"Male Students and",sum(x.count("F") for x in students),"Female Students")
  for last_name, first_name, c, gen,gpa in students:
      if c == 10:
        print("Juniors")
        print(first_name,last_name)
        continue
        print(students)
#Print students with higher than average GPA  /  print Average GPA, first name, last name, GPA
elif ans=="4":
  #for each value in students it devides by the sum of all students to get the average gpa
  for last_name, first_name, c, gen,gpa in students: 
    avg_gpa=float(sum(gpa_grade)/16)
    if gpa < 3.03:
      print("Average GPA:""{:12.2f}".format(avg_gpa))
      print("")
      break
  for last_name, first_name, c, gen,gpa in students:
      if gpa > 3.03:
        print(first_name,last_name,gpa)
#Ascending sort by last name – print first name, last name, year, GPA)
elif ans=="5":
    #function printed out
    ascending_sort_by_last_name(students)
#Print students with the highest and lowest GPA  
elif ans=="6":
    print_students_descending_gpa(students)
#Search by student last name, print first name, last name, gender, year, GPA. Print message if student is not found
elif ans=="7":
  search=input("Which student would you like to find?(Search by Last Name with a captial. Ex:White)")
  for a,b,c,d,e in students:
    if search in a:
      print(b,a,",Gender",d,",Grade",c)
elif ans=="8":
    "Thanks for your participation"
#if user inputs a number not in the choice
else:
    print(" Not a Valid Choice Try again. Please run the program again ")

    
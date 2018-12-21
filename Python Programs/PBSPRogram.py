# Welcome to my PBS Pledge Program
 # 10/15/2018
 #person_name, total_pledge-integer, amount-sentry varible 
 #program that calculates the amount a person pledged 

print ("Welcome to my pledge counter program")

#Asks the user their name
person_name = input("\nWhat is your name?")

#aks the user the amount of money they pledged
total_pledge = int(input("\nHow much money did you pledge?"))

#initializes the sentry varible
amount = 1

#while "the ammout" is greater than or equal to 1
while amount >= 1:
  #This adds 1 more amount in the loop
  amount + 1
  
  #prints out the amounts
  print ("\nPBS Pledge Summary Report\n" "\nTotal # of Donators\t", amount, "\nTotal Pledges\t\t",amount * total_pledge,
               "\nAverage pledge\t\t", total_pledge/amount)
 #this stops the loop from running forvere 
  break 


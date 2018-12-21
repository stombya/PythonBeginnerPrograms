

#Random Module that will import it.
import random

#Welcome amessage
print  ("Welcome to the Guess The number!")
print  ("\nYou will have limited tries so guess carefully!.\n")

#varible that is my varible for amount tries person does
tries = 1

#range of numbers with 75+1
number = random.randrange(75) + 1

guess = int(input("Take a guess:"))

#while loop for repeating the guess amounts

while (guess != number):
     if tries  > 5:
         break
     elif guess > number:
         print ("Lower...")
     elif guess < number:
         print ("Higher...")

 #this is the varible that tells person to ask again
     guess = int(input("Guess again:"))
     tries += 1
 
#tells the person the actual number
print("Good Job. The number was", number)
print("it only took you", tries, "tries\n")

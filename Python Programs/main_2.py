#Alex Stomberg
#12/12/18
#Peiod 7, Python Programming
#the global varibles are cs1,df1, and hd1. welcome() is the print message, calculations() multiplies each global varible with the user input. display() outputs each column


#global varible
cs1= 15
df1= 20
hd1= 12
def welcome():
  print("welcome to the stock report program")

#function for the inputs
def inputs():
  name=input("\nWhat's your Name? ")
  cs= float(input("What is the current price of Columbia Sportswear?"))
  df= float(input("What is the current price of Dean Foods?"))
  hd = float(input("What is the current price of Harley Davidson? "))
  return name,cs,df,hd

#function that calculates the stock price
def calculations(cs2,df2,hd2):
  price_col=cs2*cs1
  price_dean=df2*df1
  price_harley=hd2*hd1
  return price_col,price_dean,price_harley

  #function that display the column. It rounds the final cost of each stock.
def display(name,price_col,price_dean,price_harley,cs2,df2,hd2):
    print("\nWall Street Society")
    print("Treasurer:",name) 
    print("Company Name\t\t# of Shares\t\tPrice\t\t\tCurrent Value")
    print("Columbia Sportswear\t",cs1,"\t\t\t",cs2,"\t\t\t ",str(round(price_col,2)))
    print("Dean Foods\t\t    ",df1,"\t\t\t",df2,"\t\t\t",str(round(price_dean,2)))
    print("Harley Davidson\t\t",hd1,"\t\t\t",hd2,"\t\t\t ",str(round(price_harley,2)))

#main function that defines other varibles in the other functions. the while loop is there if the user wants to run the program again.
def main():
  welcome()
  repeat = True
  while repeat:
    name,cs,df,hd=inputs()
    price_col,price_dean,price_harley=calculations(cs,df,hd)
    display(name,price_col,price_dean,price_harley,cs,df,hd)
    choice = input("\nWould you like to run the program again (y or n)? ")
    if choice == 'n' or choice == 'N':
      repeat = False
      print()
      print("Thank you...")
main()


input("\n\nPress the enter key to exit.")


      

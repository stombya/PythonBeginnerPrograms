cs1= 15
df1= 20
hd1= 12
def welcome():
  print("welcome to the stock report program")

def inputs():
  name=input("\nWhat's your Name? ")
  cs= float(input("What is the current price of Columbia Sportswear?"))
  df= float(input("What is the current price of Dean Foods?"))
  hd = float(input("What is the current price of Harley Davidson? "))
  return name,cs,df,hd

def calculations(cs2,df2,hd2,name2):
  price_col=cs2*cs1
  price_dean=df2*df1
  price_harley=hd2*hd1
  name2=name
  return price_col,price_dean,price_harley,name2
def display(price_col,price_dean,price_harley,cs2,df2,hd2,name2):
    print("wall Street Society")
    print("Treasurer:",name2)
    print("Company Name\t\t# of Shares\t\tPrice\t\t\tCurrent Value")
    print("Columbia Sportswear\t",cs1,"\t\t\t",cs2,"\t\t\t",str(round(price_col,2)))
    print("Dean Foods\t\t",df1,"\t\t\t",df2,"\t\t\t",str(round(price_dean,2)))
    print("Harley Davidson\t\t",hd1,"\t\t\t",hd2,"\t\t\t",str(round(price_harley,2)))

def main():
  welcome()
  repeat = True
  while repeat:
    name,cs,df,hd=inputs()
    price_col,price_dean,price_harley=calculations(cs,df,hd,name2)
    display(price_col,price_dean,price_harley,cs,df,hd,name2)
    choice = input("\nWould you like to run the program again (y or n)? ")
    if choice == 'n' or choice == 'N':
      repeat = False
      print()
      print("Thank you...")
main()

# Welcome to my calculations program
# Alex Stomberg
 # Period 7 #
 # 10/5/2018
 #year_income

print = "welcome to my Tax calculations program"
#asks the user their income
year_income = int(input("\nWhat is your yearly income:"))


#this is the if statment that decideds if the income is greater than 0 but less than equal to 8925
if year_income >= 0 and year_income <= 8925:
    print("Based on your annual income of ${0:.2f}".format(year_income),
           "you owe the IRS $0 Please make your checks payable to Mr. Van Diepen.")

#elif statments that print out the same thing about the income program goes to elif when the if staements dont work
elif year_income > 8925 and year_income <= 36250:
    print("Based on your annual income of ${0:.2f}".format(year_income),
      "you owe the IRS ${0:.2f}".format((year_income*0.15)+892.50), "Please make your checks payable to Mr. Van Diepen.")

elif year_income > 36250 and year_income <= 87850:
    print("Based on your annual income of ${0:.2f}".format(year_income),
      "you owe the IRS ${0:.2f}".format((year_income*0.25)+4991.25), "Please make your checks payable to Mr. Van Diepen.")

elif year_income > 87850 and year_income <= 183250:
    print("Based on your annual income of ${0:.2f}".format(year_income),
      "you owe the IRS ${0:.2f}".format((year_income*0.28)+17891.25), "Please make your checks payable to Mr. Van Diepen.")

elif year_income > 183250 and year_income <= 298350:
    print("Based on your annual income of ${0:.2f}".format(year_income),
      "you owe the IRS ${0:.2f}".format((year_income*0.33)+44603.25), "Please make your checks payable to Mr. Van Diepen.")

elif year_income > 298350 and year_income <= 400000:
    print("Based on your annual income of ${0:.2f}".format(year_income),
      "you owe the IRS ${0:.2f}".format((year_income*0.35)+82586.25), "Please make your checks payable to Mr. Van Diepen.")

elif year_income > 400000:
    print("Based on your annual income of ${0:.2f}".format(year_income),
      "you owe the IRS ${0:.2f}".format((year_income*0.396)+118163.75), "Please make your checks payable to Mr. Van Diepen.")

else:
    print("You entered an invalid number. Please run the program again")
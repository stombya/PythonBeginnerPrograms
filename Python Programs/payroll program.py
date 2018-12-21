#Alex Stomberg
#9/19/18
#Payroll Program
#This calculates the payroll of employees then calculates the pay after tax
#

amount_hrs = float(input("How many hours did this employee work?")


katherine_smith = float(8.35)
desiree_jones = float(15.50)
daniel_kapur = float(13.25)
ruben_ramirez = float(13.50)


gross_pay1 =float(katherine_smith*amount_hrs)
social_tax1 = float(0.07*gross_pay1)
fed_tax1 = float(0.15*gross_pay1)
Net_pay1 = float(gross_pay1-social_tax1+fed_tax1)


gross_pay2 =float(desiree_jones *amount_hrs)
social_tax2 = float(0.07*gross_pay2)
fed_tax2 = float(0.15*gross_pay2)
Net_pay2 = float(gross_pay2-social_tax2+fed_tax2)

gross_pay3 =float(daniel_kapur *amount_hrs)
social_tax3 = float(0.07*gross_pay3)
fed_tax3 = float(0.15*gross_pay3)
Net_pay3 = float(gross_pay3 - social_tax3 + fed_tax3)

gross_pay4 =float(ruben_ramirez *amount_hrs)
social_tax4 = float(0.07*gross_pay4)
fed_tax4 = float(0.15*gross_pay4)
Net_pay4 = float(gross_pay4 - social_tax4 + fed_tax4)

print("Name:\t\t\t Katherine Smith")
print("Pay Rate:\t\t 8.35")
print("Hours worked:\t\t "+amount_hrs)
print("Gross Pay:\t\t"+gross_pay1)
print("\nDeductions")
print("\t\tSocial Security\t"+social_tax1)
print("\t\tFedral Tax\t"+fed_tax1)
print("\nNet pay:\t\t\t"+Net_pay1)



# Ask user for name
name = input("What is your name?:")
print("Alex")

#Ask user for their age
age = input("How old are you?:")
print("16")


#Ask user for city
city=input("What city do you live in?:")


#Ask user what they enjoy
love=input("What do you love doing?:")


#create output text

string = "Your name is {} and you are {} years old. YOu live in {} and you love {}"
output = string.format(name,age,city,love)

#Print output to screen
print(output)

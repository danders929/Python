from datetime import date

# User input functions. Each function has customized error handling
def nameCheck():
    name = input("\nEnter name: ")
    if len(name)>32:
        name = input("\nPlease limit your name to 32 characters. \nWhat is your Name? ")
    return name
def ageCheck():
    age = input("How old are you? ")
    while True:
        try:
            age = int(age)
            if age<1:
                age = input("\nHow are you even alive right now? \n Please enter your age: ")
            else:
                break
        except ValueError:
            age  = input("\nPlease use a numerical format. \nHow old are you? ")
    return int(age)
def numCheck():
    n = input("Enter a number between 1 and 10: ")
    while True:
        try:
            n = int(n)
            while n<1 or n>10:      
                n = int(input("\nPlease pick a number between 1 and 10: "))
            else:
                break
        except ValueError:
            n = input("\nInput must be in numerical format. \nPlease pick a number between 1 and 10 :")
    return int(n)

# Calls the various functions and assigns them to a variable. 
name = nameCheck()
age  = ageCheck()
n = numCheck()

# Gets the current year and uses that to output a message that will  
# tell the user when the user will turn 100. Repeats the message x
# number of times and then exits program.
today = date.today()
year = today.year
y100 = year - int(age) + 100

if age>=120:
    print ("\nYou are the oldest person alive!\n" * n)

elif age>100 and age<120:
    print ("\nCongratulations %s you made it past 100 on the year %s.\n" % (name,y100) * n)

elif age==100:
    print ("\nCongratulations %s you turned 100 this year! \n" % (name) * n)

else: 
    print ("\nHi %s! \nDid you know, you will turn 100 on the year %s\n" % (name, y100) * n)


     




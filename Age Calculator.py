from datetime import date

# User input functions. Each function has customized error handling
def nameCheck():
    name = input("enter name: ")
    if len(name)>32:
        name = input("\nPlease limit your name to 32 characters. \nWhat is your Name? ")
    return name
def ageCheck():
    age = input("How old are you? ")[:3]
    while True:
        try:
            age = int(age)
            break
        except ValueError:
            age  = input("\nPlease use a numerical format. \nHow old are you? ")[:3]
        break
    return age
def numCheck():
    n = input("Enter a number between 1 and 10: ")[:2]
    while True:
        try:
            n = int(n)
            if isinstance(n,int):
                if n<1 or n>10:           
                    n = input("\nPlease pick a number between 1 and 10: ")[:2]
                elif n>1 and n<10:
                    break
                break
            else:
                n = input("\nInput must be in numerical format. \nPlease pick a number between 1 and 10 :")[:2]
        except ValueError:
            n = input("\nPlease pick a number between 1 and 10: ")[:2]
        break
    return n

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

if int(age)>=120:
    print ("\nDamn you are the oldest person alive!\n" * n)

elif int(age)>100 and age<120:
    print ("\nCongratulations %s you made it past 100 on the year %s.\n" % (name,y100) * int(n))

elif int(age)==100:
    print ("\nCongratulations %s you turned 100 this year! \n" % (name) * int(n))

else: 
    print ("\nHi %s! \nDid you know, you will turn 100 on the year %s\n" % (name, y100) * int(n))


     




print("****************************************************************************\n")
#user input and error checking    
num = input("Enter a number: ")
while True: 
    try:
        num = int(num)
        break
    except ValueError:
        num = input("\nMust be in numerical format. \nPlease enter a number: ")

check = input("\nEnter a number you think the first number is divisible by: ")
while True: 
    try:
        check= int(check)
        break
    except ValueError:
        check = input("\nMust be in numerical format. \nPlease try another number: ")
print("----------------------------------------------------------------------------\n")

# Logical tests to verify if the number is even/odd, multiple of four, and if the first number can be divided by the second. 
# Also added tests for the value of 0 for either input. 
if num == 0:
    print("If I have %s apples and divide them evenly among %s people. No one would get any apples silly!\n" % (num,check))
    exit()
if check == 0:
    print("Attempting to divide by 0 has caused a black hole to form near the Large Hadron Colider. Congratulations you just doomed us all!\n")
    exit()
if num % 4 == 0 and num != 0:
    print("%s is a multiple of 4\n" % (num))
elif num % 2 == 0 and num != 0:
    print("%s is an even number\n" % (num))
elif num % 2 != 0 and num != 0:
    print("%s is an odd number\n" % (num))
if num % check == 0 and num != 0:
    print("%s is divisible by %s\n" % (num,check))
if num % check != 0 and num != 0:
    print("%s is not divisible by %s\n" % (num,check))
print("****************************************************************************\n")    

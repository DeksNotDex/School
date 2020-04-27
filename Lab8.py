def validVoter():
    name = input("What is your name?")
    age = int(input("How old are you %s?" % name))
    if age >= 18:
        return True
    elif age > 100:
        return ("You are not an elf")
    elif age < 0:
        return ("You cant be a negative age")
    else:
        return False

def display():
    if validVoter():
        print("You are of age!")
    else:
        print("You are not of age!")

def leapCheck(year):
    if year % 100 == 0:
        print("Not a leap year")
        return False
    elif year % 400 == 0:
        return True
    else:
        print("It is a leap year")
        return True
def isLeapYear():
    year = int(input("What year do you want to see if it is a leap year?"))
    if year % 4 == 0:
        leapCheck(year)
    else:
        print("Not a leap year")
    
               
               
               
               
               
main()

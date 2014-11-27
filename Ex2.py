###Henry Nolan-Clutterbuck
###27/11/2014
###Revision Ex 2

def usernumber():
    number = int(input("Please enter an odd number"))
    if number % 2 == 0:
        print("This number is not odd please enter another number")
    else:
        print("Your number is correct your pyramid will be displayed shortly")
    return number

def pyramid(number):
    for count in range(number,0,-2):
        print(number*("*"))
        number = (number-2)

        

pyramid(5)

def factorial(number):
    if number==1:
        return number
    else:
        return number*factorial(number-1)
number=int(input("enter your number to calculate factorial"))
if number<0:
    print("fractorial does not exist for negative numbers")
elif number==0:
    print("the factorial of 0 is 1")
else: 
    print("the factorial is ",factorial(number))         



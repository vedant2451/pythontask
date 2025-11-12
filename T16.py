# create factorial function

def factorial(n):
    if n == 0:
        return 1
    else :
        fact = 1
        for i in range(1,n+1):
           fact = fact * i

    return fact


y = int(input("enter the number : "))
x = factorial(y)
print(x)

"""
2. Prime Number Checker

Task: Write a function is_prime(num) that returns True if the number is prime, otherwise False.
"""

def is_prime(num):
    for i in range (2,num) :
        if num % i == 0:
            return False
    return True

x = int(input("Enter a number: "))
y = is_prime(x)
print(y)
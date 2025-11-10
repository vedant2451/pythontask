"""
4. Fibonacci Sequence

Task: Write fibonacci(n) → returns first n numbers in Fibonacci sequence.
"""

def fibonacci(n):

    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        list1 = [0,1]
        a=0
        b=1
        for i in range (2,n):
            z = a+b
            a = b
            b = z
            list1.append(z)

    return list1

x = int(input("Enter a number: "))
print(fibonacci(x))
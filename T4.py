# find value is divisible by 3 and 5 or divisible by 3 or divisible 5
x = int(input("Enter a number: "))
if (x%3 == 0) and (x%5 == 0):
    print(f"{x} is divisible by 3 and 5")
elif x%3 == 0 :
    print(f"{x} is divisible by 3 ")
elif x%5 == 0 :
    print(f"{x} is divisible by 5 ")
else :
    print(f"{x} is not divisible by 3 and 5")
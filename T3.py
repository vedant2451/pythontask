# compare xyz in which who has bigger value
x = int(input("Enter a number x: "))
y = int(input("Enter a number y: "))
z = int(input("Enter a number z: "))
if (x > y) and (x > z):
    print("x is greater than y and z")

elif (y > x) and (y > z):
    print("y is greater than x and z")

elif x==y==z:
    print("x and y and z  are equal")
elif x == y:
    print("x is equal to y")
elif y == z :
    print("y is equal to  z")
elif x == z :
    print("x is equal to z")

else:
    print("z is greater than x and y")

# create list with 10 element and function has two input operation(+,-,*,/) and value ,
# use input in function do operation on list with value
list1= [10,30,46,57,28,49,89,20,56,27]
list2 = []
def operation(opt,x) :
    if opt == "+":
        for i in list1 :
            list2.append(i+x)
            print(list2)
    elif opt == "-":
        for i in list1 :
            list2.append(i-x)
            print(list2)
    elif opt == "*":
        for i in list1 :
            list2.append(i*x)
            print(list2)
    elif opt == "/":
        for i in list1 :
            list2.append(i/x)
            print(list2)
    else:
        print("Please enter a valid operation")

a = int(input("Enter number: "))
o = input("Enter operation: ")
operation(o,a)
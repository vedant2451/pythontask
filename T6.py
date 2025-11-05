# create list with 10 element and add divisible by 3 element in new list
list1 = []
list2 = []


for i in  range (10) :
    a = int(input("Enter a number : "))
    list1.append(a)
print(list1)
for i in list1 :
    if i % 3 == 0 :
        list2.append(i)
print(list2)
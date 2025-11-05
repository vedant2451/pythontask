# addition of given two list each element with same index and add in empty list using while loop
list1 = [10,12,14,16,20,21,24,26]
list2 = [11,12,13,14,22,26,29,30]
list3 = []
while len(list3)<5 :
    list3.append(list1[len(list3)]+list2[len(list3)])
print(list3)
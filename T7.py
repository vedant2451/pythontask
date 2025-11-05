# Create two list and compare two list and  add same element in empty
list1 = [10,12,14,16,20,21,24,26,35,78,56,90,23,13,89]
list2 = [24,35,12,57,89,20,56]
list3 = []
for i in list1 :
    for j in list2 :
        if i ==j :
            list3.append(i)
print(list3)
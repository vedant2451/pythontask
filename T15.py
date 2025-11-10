"""
5. Remove Duplicates from List

Task:
Write a function remove_duplicates(lst) that returns a list without duplicate elements.
"""
def remove_duplicates(lst):
    result = []
    for i in lst:
        if i not in result:
            result.append(i)
    return result

#list1 = []
list2 = [10,50,10,40,50,40,40,50,10,30,60,90]
"""for i in range (10):
    a = int(input("Enter 10 numbers : "))
    list1.append(a) """
b = remove_duplicates(list2)
print(b)

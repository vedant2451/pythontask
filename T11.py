""" 1. Grade Calculator

Task: Create a function calculate_grade(marks) that takes a list of marks and returns a letter grade:

90+ → A

80–89 → B

70–79 → C

below 70→Fail
"""

def calculate_grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 80:
        return "B"
    elif marks >= 70:
        return "C"
    else :
        return "Fail"


list1 = [40,70,89,79,69,90,95]
list2 = []
for i in list1:
   z= calculate_grade(i)
   list2.append(z)
print(list2)
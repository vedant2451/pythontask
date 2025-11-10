""" 3. Count Vowels in a String

Task: Write a function count_vowels(text) that counts and returns the number of vowels.
"""

def count_vowels(text):
    count = 0
    for i in text:
        if i in "aeiouAEIOU":
            count += 1
    return count

str1 = input("Enter a string: ")
print(count_vowels(str))
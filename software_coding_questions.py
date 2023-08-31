'''
Section 2: Coding Qs

2.1 A)
Write a function that takes in a string and returns the number of
unique consonants [10 marks]
EXAMPLE INPUT: “cat”
EXAMPLE OUTPUT: 2 (‘c’ and ‘t’ are both unique)
EXAMPLE INPUT: “cataract”
EXAMPLE OUTPUT: 1 (‘r’ is the only unique consonant)
'''


def count_unique_consonants(input_string):
    consonants = "bcdfghjklmnpqrstvwxyz"  # List of consonants
    consonants_found = set()  # Set of consonants found
    unique_consonants = set()  # Set of unique consonants

    for char in input_string.lower():
        if char in consonants and char not in unique_consonants:
            if char in consonants_found:
                consonants_found.remove(char)
                unique_consonants.add(char)
            else:
                consonants_found.add(char)

    return len(consonants_found)


print(count_unique_consonants("cat"))  # Output should be 2 ("c" and "a")
print(count_unique_consonants("cataract"))  # Output should be 1 ("r")


"""
2.1 B) 
The time space complexity of the solution is O(n). 
This is because the time complexity is determined by the length of the input string. 
The set is only looped through once.
"""


"""
2.2 Write a function that finds how many squares are in a X by X grid.
For example a 2x2 Grid has 5 squares.
"""


def count_squares(x):
    total_squares = 0
    for i in range(1, x + 1):
        total_squares += i ** 2
    return total_squares


print(count_squares(2))  # Output should be 5
print(count_squares(3))  # Output should be 14


# Recursion attempt??

def count_squares2(x):
    if x == 1:
        return 1
    else:
        return x ** 2 + count_squares2(x - 1)


print(count_squares2(2))  # Output should be 5
print(count_squares2(3))  # Output should be 14

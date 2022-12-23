"""
Given two strings, find the number of common characters between them.
"""

# make sets for each string
# find the intersection of these two sets
# however, some tests will fail for this function


def char_counter(s1, s2):
    set1 = set(s1)
    set2 = set(s2)
    intersection = set1 & set2
    return intersection


"""
Given two strings, find the number of common characters between them.
This function takes into account the frequency of each string, no counting twice.
"""


def char_counter_2(s1, s2):
    # Create dictionaries to store the frequency of each character in the strings
    frequency1 = {}
    frequency2 = {}
    # Iterate over the characters in the first string
    for c in s1:
        # If the character is not in the dictionary, add it with a frequency of 1
        if c not in frequency1:
            frequency1[c] = 1
        # If the character is already in the dictionary, increment its frequency
        else:
            frequency1[c] += 1
    # Iterate over the characters in the second string
    for c in s2:
        # If the character is not in the dictionary, add it with a frequency of 1
        if c not in frequency2:
            frequency2[c] = 1
        # If the character is already in the dictionary, increment its frequency
        else:
            frequency2[c] += 1
    # Initialize a counter for the common characters
    common = 0
    # Iterate over the characters in the first dictionary
    for c in frequency1:
        # If the character is also in the second dictionary, add the minimum of the two frequencies to the counter
        if c in frequency2:
            common += min(frequency1[c], frequency2[c])
    # Return the count of common characters
    return common

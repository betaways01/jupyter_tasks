"""
Given an array of strings, return another array containing all of its longest strings.
"""

# step 1: find the first longest string
# step 2: store it in an array; []
# step 3: find the other longest string if any (for string in inputArray) with same length as the string in step 1.
# step 4: apend that string to the previous array
# step 5: return that array with the longest strings


def solution(inputArray):
    # Find the longest string in the array
    longest_string = max(inputArray, key=len)
    # Create a new array to hold the longest strings
    longest_strings = []
    # Iterate over the input array
    for string in inputArray:
        # If the current string is equal to the longest string,
        # append it to the array of longest strings
        if len(string) == len(longest_string):
            longest_strings.append(string)
    # Return the array of longest strings
    return longest_strings

"""
Given an array of strings, return another array containing all of its longest strings.
"""


def solution(inputArray):
    # Find the longest string in the array
    longest_string = min(inputArray, key=len)
    # Create a new array to hold the longest strings
    shortest_string = []
    # Iterate over the input array
    for string in inputArray:
        # If the current string is equal to the longest string,
        # append it to the array of longest strings
        if len(string) == len(longest_string):
            shortest_string.append(string)
    # Return the array of longest strings
    return shortest_string

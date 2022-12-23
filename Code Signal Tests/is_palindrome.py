# pylint: disable=invalid-name

"""Given the string, check if it is a palindrome."""


def solution(inputString):
    # Remove all non-alphanumeric characters from the string
    palindrome = ''.join(x for x in inputString if x.isalnum())
    # Make all characters lowercase
    palindrome = palindrome.lower()
    # Check if the string is equal to its reverse
    return palindrome == palindrome[::-1]

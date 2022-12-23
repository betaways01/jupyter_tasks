"""
You are given a two-digit integer n. Return the sum of its digits.
"""

# step 1: initialize summer
# step 2: convert input to string
# step 3: add string as int


def Counter(n):
    # input to string
    string_n = str(n)
    # initialize sum
    sum = 0

    for num in string_n:
        sum += int(num)
    return sum


print(Counter(1234))

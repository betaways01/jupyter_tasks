# pylint: disable=missing-function-docstring
"""
Given a year, return the century it is in.
The first century spans from the year 1 up to and including the year 100,
the second - from the year 101 up to and including the year 200, etc.
"""


def get_century(year):
    # if a multiple of 100
    if year % 100 == 0:
        century = year // 100
    # if not a multiple
    else:
        century = year // 100 + 1
    return century

import sys


def sum_two_smallest_numbers(numbers):
    numA = sys.maxsize
    numB = sys.maxsize
    for number in numbers:
        if number >= 0:
            if number < numA:
                numB = numA
                numA = number
            elif number < numB:
                numB = number
    return numA + numB

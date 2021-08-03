import sys


def sum_two_smallest_numbers(numbers):
    small_1 = sys.maxsize
    small_2 = sys.maxsize
    for elem in numbers:
        if elem < small_1:
            small_2 = small_1
            small_1 = elem
        elif elem < small_2:
            small_2 = elem

    return small_1 + small_2

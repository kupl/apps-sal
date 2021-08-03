from heapq import nsmallest


def sum_two_smallest_numbers(numbers: int):
    """ Get the sum of the two lowest positive numbers given an array. """
    return sum(nsmallest(2, numbers))

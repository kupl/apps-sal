from heapq import nsmallest


def sum_two_smallest_numbers(numbers):
    return sum(nsmallest(2, numbers))

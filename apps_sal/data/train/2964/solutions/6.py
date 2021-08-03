import heapq


def sum_two_smallest_numbers(numbers):
    return sum(heapq.nsmallest(2, numbers))

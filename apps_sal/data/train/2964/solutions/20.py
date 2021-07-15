import heapq
def sum_two_smallest_numbers(numbers):
    two_smallests = heapq.nsmallest(2, numbers)
    return two_smallests[0] + two_smallests[1]

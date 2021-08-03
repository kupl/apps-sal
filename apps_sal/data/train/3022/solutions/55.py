import heapq


def two_highest(arg1):
    return heapq.nlargest(2, set(arg1))

import heapq


def two_highest(s):
    return False if type(s) == str else heapq.nlargest(2, set(s))

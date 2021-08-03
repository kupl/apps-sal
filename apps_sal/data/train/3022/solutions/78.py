from heapq import nlargest


def two_highest(arg1):
    return nlargest(2, set(arg1))

from heapq import nlargest


def two_highest(arg1, n=2):
    return type(arg1) is list and nlargest(n, set(arg1))

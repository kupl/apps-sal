from heapq import nlargest

def two_highest(lst):
    return isinstance(lst, list) and nlargest(2, set(lst))

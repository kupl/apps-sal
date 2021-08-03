import heapq


def max_product(a):
    first, second = heapq.nlargest(2, a)
    return first * second

from heapq import nlargest


def max_tri_sum(lst):
    return sum(nlargest(3, set(lst)))

from heapq import nsmallest


def nth_smallest(lst, n): return nsmallest(n, lst)[-1]

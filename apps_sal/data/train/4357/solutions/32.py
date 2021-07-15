from heapq import nsmallest

nth_smallest = lambda lst, n: nsmallest(n, lst)[-1]

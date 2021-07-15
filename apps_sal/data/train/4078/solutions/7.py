from heapq import nsmallest
def first_n_smallest(arr, n):
    small = nsmallest(n, arr)
    return [a for a in arr if a in small and (small.remove(a) or 1)]

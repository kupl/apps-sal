from heapq import nsmallest
def nth_smallest(arr, pos):
    return nsmallest(pos, arr)[-1]

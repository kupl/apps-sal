import heapq


def nth_smallest(arr, pos):
    x = heapq.nsmallest(pos, arr)
    print(x)
    return x[-1]

from heapq import *


def nth_smallest(arr, n):
    arr = list(set(arr))
    heapify(arr)
    if n > len(arr):
        return None
    x = 0
    for i in range(n):
        x = heappop(arr)
    return x

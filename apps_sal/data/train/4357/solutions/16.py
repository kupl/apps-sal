def nth_smallest(arr, pos):
    return __import__('heapq').nsmallest(pos, arr)[-1]

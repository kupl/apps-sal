import heapq
def nth_smallest(arr, pos):
    heap = heapq.nsmallest(pos,arr)
    return heap[-1]

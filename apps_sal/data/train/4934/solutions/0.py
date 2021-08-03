import heapq
import itertools


def sort(iterable):
    heap = list(iterable)
    heapq.heapify(heap)
    return (heapq.heappop(heap) for i in range(len(heap)))

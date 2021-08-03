from heapq import heappush, heappop


def sort(words):
    heap = []
    for w in words:
        heappush(heap, w)
    while heap:
        yield heappop(heap)

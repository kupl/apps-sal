from heapq import heapify, heappop

def sort(words):
    words = list(words)
    heapify(words)
    while words:
        yield heappop(words)

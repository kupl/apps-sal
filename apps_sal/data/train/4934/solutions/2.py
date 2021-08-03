from heapq import *


def sort(iterable):
    h = []
    for value in iter(iterable):
        heappush(h, value)
    return iter([heappop(h) for i in range(len(h))])

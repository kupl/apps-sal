from heapq import *

def add_all(a):
    n = m = 0
    heapify(a)
    while len(a) > 1:
        m = heappop(a) + heappop(a)
        n += m
        heappush(a, m)
    return n

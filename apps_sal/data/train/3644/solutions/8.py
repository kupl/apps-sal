from heapq import *


def add_all(lst):
    heapify(lst)
    res = 0
    while len(lst) >= 2:
        s = heappop(lst) + heappop(lst)
        res += s
        heappush(lst, s)
    return res

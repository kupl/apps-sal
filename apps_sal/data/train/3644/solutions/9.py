from heapq import *

def add_all(lst):

    heapify(lst)
    s = 0
    total = 0
    while len(lst) > 1:
        s = heappop(lst) + heappop(lst)
        total += s
        heappush(lst, s)

    
    return total

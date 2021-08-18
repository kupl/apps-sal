from heapq import heapify, heappush, heappop


def add_all(lst):
    heapify(lst)
    s = 0
    print(lst)
    while len(lst) > 1:
        m1 = heappop(lst)
        m2 = heappop(lst)
        s += m1 + m2
        if not lst:
            return s
        heappush(lst, m1 + m2)

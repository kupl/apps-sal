import heapq


def comb(fruits):
    heapq.heapify(fruits)
    w = 0
    while len(fruits) > 1:
        (x, y) = (heapq.heappop(fruits), heapq.heappop(fruits))
        w += x + y
        heapq.heappush(fruits, x + y)
    return w

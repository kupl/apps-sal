from heapq import heapify, heappop, heappush

def comb(fruits):
    ws = list(fruits)
    heapify(ws)
    res = 0
    while len(ws) > 1:
        w = heappop(ws) + heappop(ws)
        heappush(ws, w)
        res += w
    return res

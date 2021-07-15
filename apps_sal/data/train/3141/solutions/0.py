from heapq import heappop, heappush

def comb(fruits):
    total, heap = 0, sorted(fruits)
    while len(heap) > 1:
        cost = heappop(heap) + heappop(heap)
        heappush(heap, cost)
        total += cost
    return total

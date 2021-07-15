import heapq
def add_all(heap): 
    heapq.heapify(heap)
    sum = 0
    while len(heap) > 1:
        a, b = heapq.heappop(heap), heapq.heappop(heap)
        cost = a + b
        sum += cost
        heapq.heappush(heap, cost)
    return sum


import heapq

def add_all(xs): 
    heapq.heapify(xs)
    cost = 0
    while len(xs) > 1:
        c = heapq.heappop(xs) + xs[0]
        cost += c
        heapq.heapreplace(xs, c)
    return cost

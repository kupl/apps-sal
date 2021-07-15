from heapq import heapify, heappush, heappop

def comb(fruits):
    energy = 0
    heapify(fruits)
    while len(fruits) > 1:
        cost = heappop(fruits) + heappop(fruits)
        heappush(fruits, cost)
        energy += cost
    return energy

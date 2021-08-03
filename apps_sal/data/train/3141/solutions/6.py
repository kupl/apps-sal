from heapq import heapify, heappop, heapreplace


def comb(fruits):
    fruits = fruits[:]
    heapify(fruits)
    total_cost = 0
    for i in range(len(fruits) - 1):
        cost = heappop(fruits)
        cost += fruits[0]
        total_cost += cost
        heapreplace(fruits, cost)
    return total_cost

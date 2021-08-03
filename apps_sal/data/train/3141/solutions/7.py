from heapq import heapify, heappop, heappush


def comb(fruits):
    heapify(fruits)

    energy_total = 0
    while len(fruits) > 1:
        energy_used = heappop(fruits) + heappop(fruits)
        heappush(fruits, energy_used)
        energy_total += energy_used

    return energy_total

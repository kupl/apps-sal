from heapq import heappop, heappush


def comb(fruits):
    (total, fruits) = (0, sorted(fruits))
    for _ in range(len(fruits) - 1):
        energy = heappop(fruits) + heappop(fruits)
        heappush(fruits, energy)
        total += energy
    return total

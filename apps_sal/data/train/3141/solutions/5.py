from bisect import insort


def comb(fruits):
    fruits = sorted(fruits)
    total_cost = 0
    while len(fruits) > 1:
        cost = sum(fruits[:2])
        total_cost += cost
        del fruits[:2]
        insort(fruits, cost)
    return total_cost

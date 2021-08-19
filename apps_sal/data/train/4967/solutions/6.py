def knapsack(capacity, items):
    ratios = [float(item[1]) / item[0] for item in items]
    collection = [0] * len(items)
    space = capacity
    while True:
        best_index = ratios.index(max(ratios))
        if items[best_index][0] <= space:
            collection[best_index] += 1
            space -= items[best_index][0]
        else:
            ratios[best_index] = 0
        if all((ratio == 0 for ratio in ratios)):
            return collection

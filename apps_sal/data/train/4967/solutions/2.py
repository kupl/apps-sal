def knapsack(capacity, items):
    r = [0] * len(items)
    for i, item in sorted(enumerate(items), key=lambda x: x[1][1] / float(x[1][0]), reverse=True):
        while capacity >= item[0]:
            capacity -= item[0]
            r[i] += 1
    return r

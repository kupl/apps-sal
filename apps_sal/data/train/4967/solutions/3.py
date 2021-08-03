def knapsack(capacity, items):
    sortItems = sorted(items, key=lambda tup: (tup[1] / float(tup[0])))[::-1]
    sortCount = [(i[0], i[1], 0) for i in sortItems]
    rCap = capacity
    for i in range(len(sortCount)):
        while rCap >= sortCount[i][0]:
            sortCount[i] = (sortCount[i][0], sortCount[i][1], sortCount[i][2] + 1)
            rCap -= sortCount[i][0]
    counts = [sortCount[sortItems.index(i)][2] for i in items]
    return counts

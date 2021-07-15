def knapsack(capacity, items):
    L = sorted((-y/x, x, i) for i,(x,y) in enumerate(items))
    res = [0]*len(L)
    for _, x, i in L:
        res[i], capacity = divmod(capacity, x)
    return res

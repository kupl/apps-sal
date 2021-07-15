def knapsack(capacity, items):
    res = [0] * len(items)
    vsi = sorted(((v / s, s, c) for c, (s, v) in enumerate(items)), reverse=True)
    for _, s, c in vsi:
        res[c], capacity = divmod(capacity, s)
    return res

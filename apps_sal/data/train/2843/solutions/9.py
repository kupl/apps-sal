def pack_bagpack(scores, weights, capacity):
    loads = [0] * (capacity + 1)
    for score, weight in zip(scores, weights):
        loads = [max(l, weight <= w and loads[w - weight] + score) for w, l in enumerate(loads)]
    return loads[-1]

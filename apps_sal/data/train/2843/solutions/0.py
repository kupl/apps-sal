def pack_bagpack(scores, weights, capacity):
    load = [0] * (capacity + 1)
    for (score, weight) in zip(scores, weights):
        load = [max(l, weight <= w and load[w - weight] + score) for (w, l) in enumerate(load)]
    return load[-1]

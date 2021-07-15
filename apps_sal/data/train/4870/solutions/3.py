def redistribute_wealth(w):
    w[:] = [sum(w) / len(w)] * len(w)

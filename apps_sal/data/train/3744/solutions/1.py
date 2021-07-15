def oddest(xs):
    os = list(map(oddness, xs))
    max_o = max(os, default=None)
    return xs[os.index(max_o)] if os.count(max_o) == 1 else None

def oddness(x):
    return float('inf') if x == -1 else ~x & -~x

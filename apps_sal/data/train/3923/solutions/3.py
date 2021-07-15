from collections import Counter

def micro_world(bs, k):
    c = Counter(bs)
    ns = sorted(c)
    return sum((x + k < bigger) * c[x] for x, bigger in zip(ns, ns[1:] + [float('inf')]))


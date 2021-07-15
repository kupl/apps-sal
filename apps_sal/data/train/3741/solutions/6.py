def vector_affinity(a, b):
    denom = max(len(a), len(b))
    return sum(l == r for l, r in zip(a, b)) / float(denom) if denom else 1


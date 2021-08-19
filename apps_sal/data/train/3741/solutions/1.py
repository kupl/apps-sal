def vector_affinity(a, b):
    return sum([1.0 for (x, y) in zip(a, b) if x == y]) / max(len(a), len(b)) if max(len(a), len(b)) else 1

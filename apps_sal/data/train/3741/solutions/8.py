def vector_affinity(a, b):
    return 1.0 if a == b else sum(float(x == y) for x, y in zip(a, b)) / max(len(a), len(b))

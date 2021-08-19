def vector_affinity(a, b):
    return 1.0 if a == b else sum((1 for (m, n) in zip(a, b) if m == n)) / max(len(a), len(b))

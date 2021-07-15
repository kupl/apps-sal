def vector_affinity(a, b):
    return 1.0 if a == b else sum(1 for i, j in zip(a, b) if i == j) / float(max(len(a), len(b)))

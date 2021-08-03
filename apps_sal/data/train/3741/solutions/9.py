def vector_affinity(a, b):
    return sum([an == bn for an, bn in zip(a, b)]) / float(max(len(a), len(b))) if len(a) or len(b) else 1

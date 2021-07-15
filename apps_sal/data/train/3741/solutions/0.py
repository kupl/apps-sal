def vector_affinity(a, b):
  longer = len(a) if len(a) > len(b) else len(b)
  return len([i for i, j in zip(a, b) if i == j]) / float(longer) if longer > 0 else 1.0

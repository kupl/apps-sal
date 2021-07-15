def are_similar(a, b):
    return sorted(a) == sorted(b) and sum(i != j for i, j in zip(a, b)) in [0, 2]

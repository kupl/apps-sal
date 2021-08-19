def are_similar(a, b):
    return sorted(a) == sorted(b) and sum((1 for (x, y) in zip(a, b) if x != y)) <= 2

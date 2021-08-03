def are_similar(a, b):
    return sorted(a) == sorted(b) and sum(m != n for m, n in zip(a, b)) <= 2

def first_n_smallest(a, n):
    return [v for (_, v) in sorted(sorted(enumerate(a), key=lambda x: x[1])[:n])]

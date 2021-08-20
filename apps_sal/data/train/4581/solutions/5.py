def are_similar(a, b):
    return 3 * (sorted(a) != sorted(b)) + sum((e != b[i] for (i, e) in enumerate(a))) < 3

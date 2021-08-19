from collections import Counter


def are_similar(a, b):
    return sum((i != j for (i, j) in zip(a, b))) <= 2 and Counter(a) == Counter(b)

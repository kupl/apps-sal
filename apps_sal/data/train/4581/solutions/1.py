from collections import Counter


def are_similar(a, b):
    return sum(a_ == b_ for a_, b_ in zip(a, b)) >= len(a) - 2 and Counter(a) == Counter(b)

from collections import Counter


def pair_of_shoes(shoes):
    c = Counter()
    for (lr, size) in shoes:
        c[size] += 1 if lr else -1
    return not any(c.values())

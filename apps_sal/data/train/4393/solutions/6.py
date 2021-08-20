from collections import Counter


def repeat_sum(l):
    commons = Counter()
    for s in l:
        commons.update(set(s))
    return sum((x for (x, c) in commons.items() if c > 1))

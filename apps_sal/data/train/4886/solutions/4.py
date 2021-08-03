from collections import Counter


def find_dups_miss(arr):
    c = Counter(arr)
    return [next(i for i in range(min(c), max(c)) if i not in c), sorted(x for x in c if c[x] > 1)]

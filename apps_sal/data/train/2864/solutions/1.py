from collections import Counter


def merge_arrays(a, b):
    ca, cb = Counter(a), Counter(b)
    return [k for k in sorted(ca.keys() | cb.keys()) if (k in ca) + (k in cb) == 1 or ca[k] == cb[k]]

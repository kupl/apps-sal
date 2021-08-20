from collections import Counter


def merge_arrays(a, b):
    (C1, C2) = (Counter(a), Counter(b))
    return sorted(C1.keys() ^ C2.keys() | {k for k in C1.keys() & C2.keys() if C1[k] == C2[k]})

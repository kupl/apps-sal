from collections import Counter

def merge_arrays(a, b):
    ca = Counter(a)
    cb = Counter(b)
    return [x for x in sorted(set(ca).union(cb)) if ca[x] == cb[x] or ca[x] * cb[x] == 0]

from collections import Counter

def find_dups_miss(arr):
    C = Counter(arr)
    S = set(range(min(C), max(C)+1))
    x = (S - set(C)).pop()
    L = sorted(k for k,v in C.items() if v > 1)
    return [x, L]

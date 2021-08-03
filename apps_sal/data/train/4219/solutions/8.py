def maxlen(L1, L2):
    return maxlen(L2, L1) if L1 < L2 else max(min(L1 / 2, L2), L1 / 3)

def maxlen(l1, l2):
    l1, l2 = sorted((l1, l2))
    return max(l2 / 3, min(l2 / 2, l1))

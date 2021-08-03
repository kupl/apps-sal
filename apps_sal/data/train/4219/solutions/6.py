def maxlen(l1, l2):
    l1, l2 = sorted((l1, l2))
    return max(l2 / 3, min(l2 / 2, l1))


# one-liner
#maxlen = lambda l1, l2: max(max(l1, l2)/3, min(max(l1, l2)/2, min(l1, l2)))

def maxlen(L1, L2):
    (L1, L2) = sorted((L1, L2))
    return (L2 / 2, L1, L2 / 3)[(L2 > 2 * L1) + (L2 > 3 * L1)]

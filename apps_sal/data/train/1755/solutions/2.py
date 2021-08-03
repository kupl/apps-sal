def splitlist(lst):
    if not lst:
        return [], []

    half, n = sum(lst) >> 1, len(lst)
    lst = sorted(lst, reverse=1)
    DP = [[0] * (half + 1) for i in range(n + 1)]
    for i, v in enumerate(lst):
        for j in range(1, 1 + half):
            DP[i][j] = max(v + DP[i - 1][j - v], DP[i - 1][j]) if v <= j else DP[i - 1][j]

    acc, j = DP[-2][-1], half
    a, b = [], []
    for i in reversed(range(n)):
        v = lst[i]
        if acc != DP[i - 1][j]:
            a.append(v)
            acc -= v
            j -= v
        else:
            b.append(v)
    return a, b

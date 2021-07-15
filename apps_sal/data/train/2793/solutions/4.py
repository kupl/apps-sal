def group_size(S, D):
    a000217 = lambda n: (n + 1) * n // 2
    a002024 = lambda n: int((1 + (1 + 8 * n) ** .5) / 2)
    return a002024(D - 1 + a000217(S - 1))

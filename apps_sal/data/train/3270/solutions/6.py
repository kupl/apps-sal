def closest_pair_tonum(upper_lim):
    sq = lambda x: int(x ** 0.5) == x ** 0.5
    for i in range(upper_lim - 1, 1, -1):
        for j in range(i - 1, 1, -1):
            if sq(i + j) * sq(i - j):
                return (i, j)

def calc_tip(p, r):
    T = round(p / 10 + 0.01) * 10 // 10
    return max([T - 1, T + 1, T // 2 - 1][r], 0)

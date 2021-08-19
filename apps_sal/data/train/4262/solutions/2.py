def calc_tip(p, r):
    t = round(p / 10 + 1e-08) * 10 / 10
    return max(0, t + 1 if r == 1 else t - 1 if r == 0 else t // 2 - 1)

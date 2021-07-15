def calc_tip(p, r):
    t = (p + 5) // 10
    return max(0, {
        1: t + 1,
        0: t - 1,
        -1: t // 2 - 1
    }[r])

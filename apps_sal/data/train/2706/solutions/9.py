def pass_the_bill(t, c, r):
    i = t // 2 - c + 1
    return max(i, 0) if t - r - c >= i else -1

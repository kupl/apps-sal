def pass_the_bill(t, c, r):
    return -1 if t < 2*r + 1 else max(0, t//2 + 1 - c)

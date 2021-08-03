def pass_the_bill(t, c, r): return -1 if r / t >= 0.5 else max(0, int(t / 2) + 1 - c)

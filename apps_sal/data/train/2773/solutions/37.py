def calculate_years(p, i, t, d):
    y = 0
    while p < d:
        y += 1
        cur_i = p * i * (1 - t)
        p += cur_i
    return y

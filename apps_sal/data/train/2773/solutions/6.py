def calculate_years(p, i, t, d, n=0):
    if p >= d:
        return n
    p = p + p * i * (1 - t)
    return calculate_years(p, i, t, d, n + 1)

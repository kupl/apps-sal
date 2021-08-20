def calculate_years(p, i, t, d, n=0):
    return calculate_years(p + p * i * (1 - t), i, t, d, n + 1) if p < d else n

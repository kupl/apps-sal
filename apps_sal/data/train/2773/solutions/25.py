def calculate_years(p, i, t, d):
    y = 0
    while p < d:
        p = p + p * i - p * i * t
        y += 1
    return y

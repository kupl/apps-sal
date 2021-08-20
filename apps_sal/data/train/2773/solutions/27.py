def calculate_years(p, i, t, d):
    years = 0
    while p < d:
        p = p * (1 + i) - p * i * t
        years += 1
    return years

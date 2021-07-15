def calculate_probability(n):
    return round(1 - (364 / 365) ** (n * (n - 1) / 2), 2)

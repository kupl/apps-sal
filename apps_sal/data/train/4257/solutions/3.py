def calculate_probability(n):
    count = 1
    for i in range(n):
        count *= (365 - i) / 365
    return round(1 - count, 2)

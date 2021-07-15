def series_sum(n):
    total = 0
    for i in range(n):
        total += 1 / (3 * i + 1)
    return f"{total:.2f}"

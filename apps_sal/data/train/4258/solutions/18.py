def series_sum(n):
    return f"{n and sum(1 / i for i in range(1, n*3+1, 3)):.2f}"


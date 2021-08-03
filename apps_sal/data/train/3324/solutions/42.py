def sale_hotdogs(n):
    return [n * 95, n * 100, n * 90][(n < 5) - (n > 9)]

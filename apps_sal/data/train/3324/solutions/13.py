def sale_hotdogs(n):
    return n * [0, 100, 95, 90][(n > 0) + (n >= 5) + (n >= 10)]

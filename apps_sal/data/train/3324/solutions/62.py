def sale_hotdogs(n):
    return [100, 95, 90][(n > 4) + (n > 9)] * n

def sale_hotdogs(n):
    return n * (n < 5) * 100 + n * (5 <= n < 10) * 95 + n * (n >= 10) * 90

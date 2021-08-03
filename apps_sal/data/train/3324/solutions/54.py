def sale_hotdogs(n):
    if n >= 10:
        return n * 90
    elif n < 5:
        return n * 100
    elif 5 <= n < 10:
        return n * 95

def sale_hotdogs(n):
    if 0 < n and n < 5:
        return n * 100
    elif n >= 5 and n < 10:
        return n * 95
    elif n >= 10:
        return n * 90
    else:
        return 0

def sale_hotdogs(n):
    if n < 5:
        n *= 100
    elif n < 10:
        n *= 95
    else:
        n *= 90
    return n

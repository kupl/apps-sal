def sale_hotdogs(n):
    if n <= 0:
        return 0
    if n < 5:
        return 100*n
    elif n < 10:
        return 95*n
    return 90*n

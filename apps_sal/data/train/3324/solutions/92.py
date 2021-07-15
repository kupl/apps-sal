def sale_hotdogs(n):
    if  5 <= n < 10:
        return 95 * n
    elif n < 5:
        return n * 100
    else:
        return n * 90

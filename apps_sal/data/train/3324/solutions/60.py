def sale_hotdogs(n):
    if n < 5:
        return n * 100
    elif 5 <= n < 10:
        return n * 100 - n * 5
    else:
        return n * 100 - n * 10

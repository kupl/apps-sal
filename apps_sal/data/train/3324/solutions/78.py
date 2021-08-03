def sale_hotdogs(n):
    if n < 5:
        return n * 100
    elif 5 >= n or n < 10:
        return n * 95
    elif n >= 10:
        return n * 90

def sale_hotdogs(n):
    a, b = range(0, 5), range(5, 10)
    if n in a:
        return n * 100
    elif n in b:
        return n * 95
    else:
        return n * 90

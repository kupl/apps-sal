def round_it(n):
    l, r = [len(i) for i in str(n).split('.')]

    if l < r:
        return int(n + .9)
    elif l > r:
        return int(n - .1)
    return round(n, 0)

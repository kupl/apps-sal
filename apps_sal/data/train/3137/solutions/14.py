def round_it(n):
    l, r = [len(i) for i in str(n).split('.')]

    if l < r:
        return int(n + .9)  # ceil
    elif l > r:
        return int(n - .1)  # floor
    return round(n, 0)

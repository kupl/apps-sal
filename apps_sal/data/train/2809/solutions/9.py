def digitize(n):
    d, r = divmod(n, 10)
    if d:
        return [r] + digitize(d)
    else:
        return [r]

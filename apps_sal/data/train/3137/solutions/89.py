def round_it(n):
    a = str(n).split('.')
    b = [int(x) for x in a]
    if b[0] > b[1]:
        return round(n - 0.5)
    else:
        return round(n + 0.5)

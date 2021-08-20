def round_it(n):
    (l, r) = str(n).split('.')
    pos = len(l) - len(r)
    return round(n) if pos == 0 else int(n) if pos > 0 else int(n + 1)

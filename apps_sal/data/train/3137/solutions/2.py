def round_it(f):
    n, d = str(f).split('.')
    return round(f) if len(n) == len(d) else int(n) + (len(n) < len(d))

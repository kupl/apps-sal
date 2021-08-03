def round_it(n):
    a, b = str(n).split('.')
    return int(n) + 1 if len(a) < len(b) else int(n) if len(b) < len(a) else round(n)

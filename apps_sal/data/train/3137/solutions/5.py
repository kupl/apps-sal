def round_it(n):
    (a, b) = map(len, str(n).split('.'))
    return round(n) if a == b else int(n) + (a < b)

def round_it(n):
    left, right = map(len, str(n).split('.'))
    return int(n) + 1 if left < right else int(n) if left > right else round(n)

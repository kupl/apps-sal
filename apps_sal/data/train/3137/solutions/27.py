def round_it(n):
    (left, right) = str(n).split('.')
    return round(n) if len(left) == len(right) else int(n) + (len(left) < len(right))

def min_value(digits):
    x = list(set(digits))
    x.sort()
    return int(''.join((str(x) for x in x)))

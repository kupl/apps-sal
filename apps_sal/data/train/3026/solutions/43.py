def min_value(digits):
    x = sorted(set(digits))
    y = [str(a) for a in x]
    return int(''.join(y))

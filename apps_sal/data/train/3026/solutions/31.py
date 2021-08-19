def min_value(digits):
    digits = sorted(set(digits))
    return int(''.join((str(x) for x in digits)))

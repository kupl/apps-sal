def min_value(digits):
    a = set(digits)
    a = sorted([str(i) for i in a])
    return int(''.join(a))

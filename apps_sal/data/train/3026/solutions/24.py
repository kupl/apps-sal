def min_value(digits):
    return int(''.join((str(s) for s in sorted(set(digits)))))

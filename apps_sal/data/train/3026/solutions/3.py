def min_value(digits):
    return int(''.join((str(i) for i in sorted(set(digits), reverse=False))))

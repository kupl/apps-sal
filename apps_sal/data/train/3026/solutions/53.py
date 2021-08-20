def min_value(digits):
    digits = sorted(set(digits), reverse=True)
    return sum((d * 10 ** i for (i, d) in enumerate(digits)))

def min_value(digits):
    digits = sorted(set(digits), reverse=True)
    return sum(n * 10**i for i, n in enumerate(digits))

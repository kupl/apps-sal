def min_value(digits):
    digits = sorted(set(digits), reverse=True)    # Remove duplicated and then sort the result
    return sum(d * 10**i for i, d in enumerate(digits))

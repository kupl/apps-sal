def min_value(digits):
    for i in range(0, len(digits)):
        digits[i] = str(digits[i])
    digits = set(digits)
    digits = sorted(list(digits))
    return int("".join(digits))

def min_value(digits):
    value = ''
    digits = set(digits)
    digits = sorted(digits)
    for digit in digits:
        value += str(digit)
    return int(value)


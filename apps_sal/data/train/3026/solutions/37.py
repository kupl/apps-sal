def min_value(digits):
    digits = list(set(digits))
    digits = sorted(digits)
    digits = [str(i) for i in digits]
    digits = ''.join(digits)
    return int(digits)

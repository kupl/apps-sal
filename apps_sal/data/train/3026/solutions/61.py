def min_value(digits):
    digits = sorted(list(dict.fromkeys(digits)))
    digits = ''.join(list(map(str, digits)))
    return int(digits)

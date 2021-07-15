def min_value(digits):
    new_digits = list(set(digits))
    new_digits.sort()
    res = int("".join(map(str, new_digits)))
    return res

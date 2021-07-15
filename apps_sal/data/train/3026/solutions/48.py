def min_value(digits):
    digits = sorted(set(digits))
    strings = [str(integer) for integer in digits]
    return int("".join(strings))

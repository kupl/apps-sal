def min_value(digits):
    l = sorted(str(x) for x in set(digits))
    return int("".join(l))


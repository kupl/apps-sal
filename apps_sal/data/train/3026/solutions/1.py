def min_value(digits):
    return int("".join(str(x) for x in sorted(set(digits))))

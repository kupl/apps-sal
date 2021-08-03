def min_value(digits):
    return int("".join(repr((n)) for n in sorted(set(digits))))

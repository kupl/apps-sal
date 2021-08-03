def min_value(digits):
    y = sorted(list(set(digits)))
    x = [str(i) for i in y]
    return int("".join(x))

def min_value(digits):
    array = sorted(list(set(digits)))
    return int("".join([str(i) for i in array]))

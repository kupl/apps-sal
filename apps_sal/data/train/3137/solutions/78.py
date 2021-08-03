from math import ceil, floor


def round_it(n):
    n = str(n)
    dot_index = n.find(".")
    before_dot = n[:dot_index]
    after_dot = n[dot_index + 1:]

    if len(before_dot) < len(after_dot):
        return ceil(float(n))
    elif len(before_dot) > len(after_dot):
        return floor(float(n))
    elif len(before_dot) == len(after_dot):
        return round(float(n))

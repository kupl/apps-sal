from math import ceil, floor


def round_it(n):
    s = str(n)
    if s.index(".") < len(s) // 2:
        return ceil(n)
    elif s.index(".") > len(s) // 2:
        return floor(n)
    else:
        if len(s) % 2 == 0:
            return floor(n)
        else:
            return round(n)

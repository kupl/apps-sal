from itertools import groupby


def sum_from_string(string):
    return sum((int(''.join(gp)) for (b, gp) in groupby(string, key=str.isdigit) if b))

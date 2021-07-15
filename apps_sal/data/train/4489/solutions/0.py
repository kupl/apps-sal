from itertools import groupby

def sum_consecutives(s):
    return [sum(group) for c, group in groupby(s)]

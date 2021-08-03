from itertools import groupby


def split_odd_and_even(n):
    return [int(''.join(list(gp))) for _, gp in groupby(str(n), key=lambda x: int(x) % 2)]

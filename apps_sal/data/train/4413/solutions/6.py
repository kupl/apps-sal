from itertools import groupby


def split_odd_and_even(n):
    return [int(''.join(grp)) for (_, grp) in groupby(str(n), key=lambda x: int(x) % 2)]

import re


def pair_zeros(arr, *args):
    return list(map(int, re.sub(r"(0[^0]*)0", "\\1", "".join([str(a) for a in arr]))))

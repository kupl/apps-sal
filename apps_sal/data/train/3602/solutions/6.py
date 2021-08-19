from itertools import groupby


def run_length_encoding(s):
    return [[sum((1 for _ in grp)), c] for (c, grp) in groupby(s)]

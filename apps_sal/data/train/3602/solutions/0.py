from itertools import groupby


def run_length_encoding(s):
    return [[sum((1 for _ in g)), c] for (c, g) in groupby(s)]

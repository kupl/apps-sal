from itertools import groupby


def run_length_encoding(s):
    return [[len(list(gp)), x] for (x, gp) in groupby(s)]

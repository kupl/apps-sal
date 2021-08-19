from itertools import groupby


def run_length_encoding(s):
    return [[len(list(g)), k] for (k, g) in groupby(s)]

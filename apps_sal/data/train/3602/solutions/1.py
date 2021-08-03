from itertools import groupby


def run_length_encoding(s):
    return [[len(list(b)), a] for a, b in groupby(s)]

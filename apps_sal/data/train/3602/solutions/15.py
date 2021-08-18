from itertools import groupby


def run_length_encoding(s):
    encoded_s = []

    def key(x): return x[0]

    for k, g in groupby(s, key):
        encoded_s.append([len(list(g)), k])

    return encoded_s

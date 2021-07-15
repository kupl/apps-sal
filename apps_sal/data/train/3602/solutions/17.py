from itertools import groupby

def run_length_encoding(s):
    return [[len(x), x[0]] for x in [list(g) for k, g in groupby(s)]]

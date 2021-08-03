from itertools import groupby
import re


def run_length_encoding(s):
    return [[len(list(j)), i] for i, j in groupby(s)]
    return [[len(i), j] for i, j in re.findall(r'((.)\2*)', s)]

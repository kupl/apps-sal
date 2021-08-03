import re


def run_length_encoding(s):
    return [[len(l), e] for l, e in re.findall(r'((.)\2*)', s)]

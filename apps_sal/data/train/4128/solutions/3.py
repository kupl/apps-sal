import re


def bears(n, stg):
    pairs = re.findall(r"B8|8B", stg)
    return ["".join(pairs), len(pairs) >= n]

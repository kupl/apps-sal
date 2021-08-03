import re


def bears(n, s):
    a = re.findall(r"B8|8B", s)
    return ["".join(a), len(a) >= n]

import re


def hydrate(s):
    n = sum(map(int, re.findall('\\d+', s)))
    return f"{n} glass{'es' * (n != 1)} of water"

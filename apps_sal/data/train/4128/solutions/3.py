import re


def bears(n, stg):
    pairs = re.findall('B8|8B', stg)
    return [''.join(pairs), len(pairs) >= n]

import re


def encode(s):
    return ''.join((f'{len(g)}{c}' for (g, c) in re.findall('((.)\\2*)', s)))


def decode(s):
    return ''.join((int(n) * c for (n, c) in re.findall('(\\d+)(\\w)', s)))

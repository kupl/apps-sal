def encode(s):
    return ''.join((f'{len(list(group))}{char}' for (char, group) in __import__('itertools').groupby(s)))


def decode(s):
    return ''.join((c * int(n) for (n, c) in __import__('re').findall('(\\d+)(\\D{1})', s)))

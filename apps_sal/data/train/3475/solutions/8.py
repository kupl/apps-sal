import re


def to_integer(string):
    b = '\\A[+-]?0b1+[01]*\\Z'
    x = '\\A[+-]?0x[1-9A-Fa-f]+[0-9A-Fa-f]*\\Z'
    o = '\\A[+-]?0o[1-7]+[0-7]*\\Z'
    d = '\\A[+-]?[0-9]+\\Z'
    for (pattern, base) in zip((b, x, o, d), (2, 16, 8, 10)):
        if re.search(pattern, string):
            return int(string, base)
    return None

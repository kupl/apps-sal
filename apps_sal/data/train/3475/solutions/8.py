import re


def to_integer(string):
    b = r'\A[+-]?0b1+[01]*\Z'
    x = r'\A[+-]?0x[1-9A-Fa-f]+[0-9A-Fa-f]*\Z'
    o = r'\A[+-]?0o[1-7]+[0-7]*\Z'
    d = r'\A[+-]?[0-9]+\Z'
    # print(string)
    for pattern, base in zip((b, x, o, d), (2, 16, 8, 10)):
        if re.search(pattern, string):
            return int(string, base)
    return None

from collections.abc import Iterable


def value_str(s):
    if not isinstance(s, Iterable):
        return 0
    vals = [ord(x.upper()) for x in s if x.isalpha()]
    if len(s) != len(vals):
        return 0
    return sum(vals)


def compare(s1, s2):
    return value_str(s1) == value_str(s2)

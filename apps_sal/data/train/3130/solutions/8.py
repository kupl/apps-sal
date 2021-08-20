import re


def has_subpattern(string):
    n = len(string)
    if n == 1:
        return False
    (l, h) = '{}'
    for i in range(1, n):
        if n % i == 0 and string[:i] * (n // i) == string:
            return True
    return False

import re


def repeating_fractions(n, d):
    (i, d) = str(n * 1.0 / d).split('.')
    return i + '.' + re.sub(r'([0-9])\1+', r'(\1)', d)

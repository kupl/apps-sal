import re


def repeating_fractions(n, d):
    ok = str((n + 0.0) / d).split('.')
    return ok[0] + '.' + re.sub('(\\d)\\1+', '(\\1)', ok[1])

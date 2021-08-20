import re


def repeating_fractions(a, b):
    if not a % b:
        return str(a / b)
    (a, b) = str(a / b).split('.')
    return a + '.' + re.sub('(.)\\1+', '(\\1)', b)

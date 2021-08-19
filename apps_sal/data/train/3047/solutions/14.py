import re


def repeating_fractions(q, b):
    (x, y) = str(q / b).split('.')
    return x + '.' + re.sub('(\\d)\\1+', '(\\1)', y)

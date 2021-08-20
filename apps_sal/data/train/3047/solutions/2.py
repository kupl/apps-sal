import re


def repeating_fractions(num, den):
    (d, f) = str(num / den).split('.')
    return '{}.{}'.format(d, re.sub('(\\d)\\1+', '(\\1)', f))

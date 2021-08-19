import re


def repeating_fractions(q, b):
    return re.sub('(\\d)\\1+(?!\\.)', '(\\1)', str(q / b))

import re


def happy_g(s):
    return not re.search('([^g]|\\b)g(\\b|[^g])', s)

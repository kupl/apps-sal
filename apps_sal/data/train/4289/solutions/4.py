import re


def happy_g(s):
    return not re.search('(^|[^g])[g]([^g]|$)', s)

import re


def happy_g(s):
    return bool(re.match("^(g{2,}|[^g])+$", s))

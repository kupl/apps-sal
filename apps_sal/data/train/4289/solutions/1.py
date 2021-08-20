import re


def happy_g(s):
    return re.sub('g{2,}', '', s).count('g') < 1

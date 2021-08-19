import re


def happy_g(s):
    return all((len(i) > 1 for i in re.findall('g+', s)))

import re


def count_repeats(str):
    return sum((len(i[0]) - 1 for i in re.findall('((.)\\2+)', str)))

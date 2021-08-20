import re


def sum_from_string(s):
    return sum(map(int, re.findall('\\d+', s)))

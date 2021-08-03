import re


def sum_from_string(s):
    return sum(map(int, re.findall(r'\d+', s)))

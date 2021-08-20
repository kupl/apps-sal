import re


def sum_from_string(str_):
    return sum(map(int, re.findall('\\d+', str_)))

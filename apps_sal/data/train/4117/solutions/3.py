import re

def sum_from_string(str_):
    return sum(map(int, re.findall(r'\d+', str_)))

import re

def sum_nested(lst):
    return sum(map(int, re.findall('\d+', str(lst))))


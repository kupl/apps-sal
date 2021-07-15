import re

def sum_nested(lst):
    return sum(int(x) for x in re.findall('\d+', str(lst)))

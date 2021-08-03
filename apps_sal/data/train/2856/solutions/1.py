import re


def gap(num):
    x = re.findall('(?=(10+1))', bin(num).lstrip('0b'))
    return max([len(i) - 2 for i in x]) if x else 0

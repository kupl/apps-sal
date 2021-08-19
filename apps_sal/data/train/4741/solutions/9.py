import re
from functools import cmp_to_key


def compare(a, b):
    cmp1 = a[0].isupper() - b[0].isupper()
    cmp2 = (a < b) - (a > b)
    return cmp1 or cmp2 * (-1 if a[0].islower() else 1)


def pseudo_sort(st):
    return ' '.join(sorted(re.findall('\\w+', st), key=cmp_to_key(compare)))

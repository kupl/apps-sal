import re


def infected_zeroes(lst):
    return max(((len(m) + 1) // 2 if s and e else len(m) for (s, m, e) in re.findall('(^|0)(1+)(0|$)', ''.join(map(str, lst)).replace('0', '00'))), default=0)

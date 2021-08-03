from fractions import Fraction as fr
from math import ceil


def decompose(s):
    s = str(fr(s)).split('/')
    if len(s) == 1:
        return [s, []][s[0] == '0']
    li = [[1, ceil(eval('int(s[1]) / int(s[0])'))]]
    while 1:
        n, d = li[-1]
        s = str(fr(int(s[0]), int(s[1])) - fr(n, d)).split('/')
        if len(s) == 1:
            break
        li.append([1, ceil(eval('int(s[1]) / int(s[0])'))])
    return [str(fr(f'{i}/{j}')) for i, j in li]

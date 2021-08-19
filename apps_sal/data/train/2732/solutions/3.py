from collections import Counter as C
from string import ascii_lowercase as l, digits as d


def blocks(s):
    if not s:
        return ''
    char = sorted(C(s).items(), key=lambda x: (l + l.upper() + d).index(x[0]))
    li = [''] * max(char, key=lambda x: x[1])[1]
    for (i, j) in char:
        for pos in range(j):
            li[pos] += i
    return '-'.join(li)

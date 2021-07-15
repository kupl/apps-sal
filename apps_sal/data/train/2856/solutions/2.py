import re

def gap(num):

    n = 0

    for m in re.finditer('(?=(1(0+)1))', bin(num)[2:]):
        n = max(n, m.end(2) - m.start(2))

    return n

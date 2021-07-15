import re

def infected(s):
    n = sum(map(len, re.findall(r'0*1[01]*', s)))
    s = len(s.replace('X',''))
    return s and 100*n/s

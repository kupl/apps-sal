from itertools import *


def find(s):
    r = ''
    for i in range(len(s)):
        for j in range(i, len(s) + 1):
            g = [k for k, g in groupby(s[i:j])]
            if len(g) == 2:
                if j - i > len(r):
                    r = s[i:j]
    return r

from string import ascii_lowercase as a
import re


def insert_missing_letters(s):
    t = ''
    c = set()
    for i in s:
        if i not in c:
            t = t + i + re.sub('|'.join(s), '', a[a.index(i) + 1:]).upper()
            c.add(i)
        else:
            t += i
    return t

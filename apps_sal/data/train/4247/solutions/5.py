import re


def odd(s):
    for c in range(len(s)):
        (last, s) = (s, re.sub('o(.*?)d(.*?)d', '\\1\\2', s, count=1))
        if last == s:
            return c

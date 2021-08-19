from collections import Counter
import re


def swaper(m):
    return m[0].swapcase()


def buildPattern(s):
    return f"[{''.join((c for (c, n) in Counter(s.lower()).items() if n & 1)) or ' '}]"


def player(a, b):
    return re.sub(buildPattern(b), swaper, a, flags=re.I)


def work_on_strings(a, b):
    return player(a, b) + player(b, a)

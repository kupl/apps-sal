import re
from functools import partial


def convert(match):
    n, s = match.groups()
    n = int(n)
    if n == 0 or n == 1:
        return match.group()
    elif n == 2:
        return "2 bu{}".format(s[:-1])
    elif 3 <= n <= 9:
        return "{} {}zo".format(n, s[:-1])
    else:
        return "{} ga{}ga".format(n, s[:-1])


sursurungal = partial(re.compile(r"(\d+) (\w+)").sub, convert)

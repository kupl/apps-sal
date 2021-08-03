import re


def solve(s):
    swap = reversed([m.start() for m in re.finditer(r"[^ ]", s)])
    return "".join(s[next(swap)] if c != " " else c for c in s)

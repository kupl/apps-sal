import re


def spiner(s, p):
    return (s[::-1] if len(s) > 6 or s.lower().count('t') > 1 else s.upper() if len(s) == 2 or p == ',' else '0' if len(s) == 1 else s) + p


def spin_solve(sentence):
    return re.sub("((?:\\w|['-])+)(\\W)?", lambda m: spiner(m.group(1), m.group(2) or ''), sentence)

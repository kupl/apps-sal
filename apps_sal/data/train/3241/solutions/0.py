import re


def buy_newspaper(s1, s2):
    p = re.sub(r"(.)", r"\1?", s1)
    return -1 if set(s2) - set(s1) else len(re.findall(p, s2)) - 1

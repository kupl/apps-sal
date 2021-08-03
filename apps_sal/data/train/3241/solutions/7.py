import re


def buy_newspaper(s1, s2):
    m = re.findall("".join((i + "?" for i in s1)), s2)[:-1]
    return len(m) if "" not in m else -1

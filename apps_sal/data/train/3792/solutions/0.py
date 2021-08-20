import re


def slogans(p, r):
    reg = re.compile('|'.join([p[i:] for i in range(len(p))]))
    return len(re.findall(reg, r))

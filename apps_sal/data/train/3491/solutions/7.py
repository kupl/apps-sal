import re


def substring(s):
    if len(s) < 2:
        return s
    pat = re.compile('(.)\\1*(.)(\\1|\\2)*', re.DOTALL)
    return max((pat.search(s, i).group() for i in range(len(s) - 1)), key=len)

import re


def solve(s):
    while '()' in s:
        s = re.sub('\\(\\)', '', s)
    ss = re.sub('\\(\\(|\\)\\)', '', s)
    sss = re.sub('\\)\\(', '', ss)
    return [-1, (len(s) - len(ss)) // 2 + len(ss)][not bool(sss)]

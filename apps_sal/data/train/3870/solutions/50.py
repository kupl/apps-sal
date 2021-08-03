import re


def solve(s):
    iter = re.finditer(' ', s)
    spaces = [x.start(0) for x in iter]

    s_rev = list(s[::-1].replace(' ', ''))

    for i in spaces:
        s_rev.insert(i, ' ')
    return ''.join(s_rev)

import re


def solve(s):
    reg = re.compile('\\d+')
    ans = reg.findall(s)
    val = 0
    holder = [int(x) for x in ans]
    for ele in holder:
        if ele > val:
            val = ele
    return val
    pass

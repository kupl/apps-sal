from itertools import groupby
from collections import defaultdict
tbl = str.maketrans('!?', '?!')


def replace(s):
    xs = [''.join(grp) for (_, grp) in groupby(s)]
    stacks = defaultdict(list)
    result = []
    for (i, x) in enumerate(xs):
        stack = stacks[x]
        if stack:
            result[stack.pop(0)] = x = ' ' * len(x)
        else:
            stacks[x.translate(tbl)].append(i)
        result.append(x)
    return ''.join(result)

from itertools import groupby

def find_longest(st):
    positions = []
    stack = []
    for i, ch in enumerate(st):
        if ch == '(':
            stack.append(i)
        elif stack:
            positions.append(stack.pop())
            positions.append(i)
    positions.sort()

    res = [a+1 == b for a, b in zip(positions, positions[1:])]
    ans = [len(list(g))+1 for k, g in groupby(res)]
    return max(ans, default=0)

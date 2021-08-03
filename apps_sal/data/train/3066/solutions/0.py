from functools import reduce


def solve(st):
    res, s, k = [], "", 1
    for ch in st:
        if ch == '(':
            res.append(k)
            k = 1
        elif ch == ')':
            res.pop()
            k = 1
        elif ch == '-':
            k = -1
        elif ch == '+':
            k = 1
        else:
            s += '-' + ch if (reduce(lambda a, b: a * b, res, 1) * (1 if k == 1 else -1) < 0) else '+' + ch
    return s if s[0] == '-' else s[1:]

from itertools import cycle
FIRST4 = {'fib': [0, 0, 0, 1], 'jac': [0, 0, 0, 1], 'pad': [0, 1, 0, 0], 'pel': [0, 0, 0, 1], 'tet': [0, 0, 0, 1], 'tri': [0, 0, 0, 1]}
FUNCS = {'fib': lambda a: a[-1] + a[-2], 'jac': lambda a: a[-1] + 2 * a[-2], 'pad': lambda a: a[-2] + a[-3], 'pel': lambda a: 2 * a[-1] + a[-2], 'tet': lambda a: a[-1] + a[-2] + a[-3] + a[-4], 'tri': lambda a: a[-1] + a[-2] + a[-3]}


def zozonacci(p, n):
    if n == 0 or not p:
        return []
    a = FIRST4[p[0]][:n]
    fs = cycle(map(FUNCS.get, p))
    for i in range(n - 4):
        a.append(next(fs)(a))
    return a

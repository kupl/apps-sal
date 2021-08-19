from itertools import cycle
ROOT = {'fib': [0, 0, 0, 1], 'jac': [0, 0, 0, 1], 'pad': [0, 1, 0, 0], 'pel': [0, 0, 0, 1], 'tet': [0, 0, 0, 1], 'tri': [0, 0, 0, 1]}
GEN = {'fib': lambda a: a[-1] + a[-2], 'jac': lambda a: a[-1] + 2 * a[-2], 'pad': lambda a: a[-2] + a[-3], 'pel': lambda a: 2 * a[-1] + a[-2], 'tet': lambda a: a[-1] + a[-2] + a[-3] + a[-4], 'tri': lambda a: a[-1] + a[-2] + a[-3]}


def zozonacci(pattern, n):
    if not pattern or not n:
        return []
    lst = ROOT[pattern[0]][:]
    cycl = cycle(map(GEN.get, pattern))
    for (f, _) in zip(cycl, range(n - 4)):
        lst.append(f(lst))
    return lst[:n]

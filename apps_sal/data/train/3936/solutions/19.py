from itertools import cycle


def zozonacci(p, n):
    if not p or not n:
        return []
    formula = {'fib': lambda: a[-1] + a[-2], 'jac': lambda: a[-1] + 2 * a[-2], 'pad': lambda: a[-2] + a[-3], 'pel': lambda: 2 * a[-1] + a[-2], 'tet': lambda: sum((a[-i] for i in range(1, 5))), 'tri': lambda: sum((a[-i] for i in range(1, 4)))}
    a = [0, 1, 0, 0] if p[0] == 'pad' else [0, 0, 0, 1]
    if n <= 4:
        return a[:n]
    i = 0
    p = cycle(p)
    while i < n - 4:
        a.append(formula[next(p)]())
        i += 1
    return a

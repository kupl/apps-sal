from itertools import cycle


def nacci(coef):
    return lambda seq: sum(c * a for c, a in zip(coef, seq[-4:]))


def zozonacci(pattern, length):
    if not pattern:
        return []
    d = {'fib': nacci([0, 0, 1, 1]),
         'pad': nacci([0, 1, 1, 0]),
         'jac': nacci([0, 0, 2, 1]),
         'pel': nacci([0, 0, 1, 2]),
         'tri': nacci([0, 1, 1, 1]),
         'tet': nacci([1, 1, 1, 1])
         }
    c = cycle(map(d.get, pattern))
    res = ([0, 1, 0, 0] if pattern[0] == 'pad' else [0, 0, 0, 1])[:length]
    for _ in range(length - 4):
        res.append(next(c)(res))
    return res

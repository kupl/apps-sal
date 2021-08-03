from itertools import product


def sat(f: Formula):
    def t(f, s=set()): return s.add(f) or s if f.is_literal() else list(map(t, f.args)) and s
    def e(f, d): return d[f] if f.is_literal() else any(e(n, d)for n in f.args) if f.is_or() else all(e(n, d)for n in f.args) ^ f.is_not()
    lst = list(t(f))
    return next(({n for n in d if d[n]} for p in product([0, 1], repeat=len(lst)) for d in [dict(zip(lst, p))] if e(f, d)), False)

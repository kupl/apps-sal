from itertools import combinations
from typing import Iterable, List


def literals(f: Formula) -> List[Literal]:
    if f.is_literal():
        return [f]
    return [x for g in f.args for x in literals(g)]


def evaluate(f: Formula, i: Iterable[Literal]) -> bool:
    if f.is_literal():
        return f in i
    if f.is_not():
        return not evaluate(f.args[0], i)
    args = (evaluate(g, i) for g in f.args)
    if f.is_and():
        return all(args)
    if f.is_or():
        return any(args)


def sat(f: Formula):
    lits = set(literals(f))
    n = len(lits)
    for r in range(0, n + 1):
        for i in combinations(lits, r):
            if evaluate(f, set(i)):
                return set(i)
    return False

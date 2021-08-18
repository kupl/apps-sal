from collections import defaultdict
from functools import reduce
import re

P_EQ = re.compile("(?P<eq>=)|(?P<coef>[+-]?\d*)(?P<var>[a-zA-Z]*)")


def solve(*equations):

    eqsMap = list(map(parse, equations))
    vars = reduce(set.union, (set(e) for e in eqsMap))
    vars = list(set(vars) - {''}) + ['']

    if len(vars) - 1 > len(equations):
        return None

    m = [[eqm[v] for v in vars] for eqm in eqsMap]

    return solveMatrix(m, vars)


def parse(eq):
    rev, dct = 1, defaultdict(int)
    for m in P_EQ.finditer(eq.replace(" ", "")):
        if m['eq']:
            rev = -1
        else:
            gc, gv = m['coef'], m['var']
            if gc or gv:
                coef = 1 if not gc or gc == '+' else -1 if gc == '-' else int(gc)
                dct[m['var']] += coef * rev
    return dct


def solveMatrix(m, vars):

    EPS = 1e-10
    pivots = {}
    toDo = set(range(len(m)))

    for y in range(len(vars) - 1):

        _, px = max(((abs(m[x][y]), x) for x in toDo if abs(m[x][y]) > 0), default=(-1, -1))

        if px == -1:
            continue
        pivots[px] = y
        toDo.remove(px)

        maxP, m[px][y] = m[px][y], 1
        for j in range(y + 1, len(vars)):
            m[px][j] /= maxP
            if abs(m[px][j]) < EPS:
                m[px][j] = 0

        for x in range(0, len(m)):
            if x == px:
                continue

            coef, m[x][y] = m[x][y], 0
            for j in range(y + 1, len(vars)):
                m[x][j] -= coef * m[px][j]
                if abs(m[x][j]) < EPS:
                    m[x][j] = 0

    solvedDct = {}
    for x in range(len(m)):
        yP = pivots.get(x, None)
        if yP is None:
            continue

        solvedDct[vars[yP]] = -m[x][-1]

    if len(solvedDct) == len(vars) - 1:
        return solvedDct

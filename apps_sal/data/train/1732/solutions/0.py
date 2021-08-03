from collections import defaultdict
from functools import reduce
import re

P_EQ = re.compile("(?P<eq>=)|(?P<coef>[+-]?\d*)(?P<var>[a-zA-Z]*)")


def solve(*equations):

    eqsMap = list(map(parse, equations))                         # Transform each string in a dict {'var': coef}
    vars = reduce(set.union, (set(e) for e in eqsMap))         # Extract all the variables
    vars = list(set(vars) - {''}) + ['']                         # Push the "constants" at the end of the list

    if len(vars) - 1 > len(equations):
        return None                 # Not enough equations to solve the system

    m = [[eqm[v] for v in vars] for eqm in eqsMap]              # Build the matrix

    return solveMatrix(m, vars)                                  # Solve using Gauss elimination


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
    pivots = {}                                                  # dict of the indexes of the pivots (avoid to have to move the raws)
    toDo = set(range(len(m)))                                  # set with the indexes of all the lines where the pivot will have to be sought for

    for y in range(len(vars) - 1):                                 # "-1" to avoid the constants

        _, px = max(((abs(m[x][y]), x) for x in toDo if abs(m[x][y]) > 0), default=(-1, -1))

        if px == -1:
            continue                                    # No pivot found
        pivots[px] = y
        toDo.remove(px)

        maxP, m[px][y] = m[px][y], 1
        for j in range(y + 1, len(vars)):                           # Update the line of the current pivot
            m[px][j] /= maxP
            if abs(m[px][j]) < EPS:
                m[px][j] = 0                 # Handle floating point errors

        for x in range(0, len(m)):                                # Update all the lines, doing the elimination
            if x == px:
                continue                                   # Skip the line of the current pivot

            coef, m[x][y] = m[x][y], 0
            for j in range(y + 1, len(vars)):                       # Update the line of the current pivot
                m[x][j] -= coef * m[px][j]
                if abs(m[x][j]) < EPS:
                    m[x][j] = 0               # Handle floating point errors, again...

    solvedDct = {}
    for x in range(len(m)):                                      # Build the solution dict
        yP = pivots.get(x, None)
        if yP is None:
            continue

        solvedDct[vars[yP]] = -m[x][-1]

    if len(solvedDct) == len(vars) - 1:
        return solvedDct           # Valid only if all the variables have been used as pivots

import re
from functools import reduce


def parse_term(term, scale):
    parts = re.findall('[+-]?\\d+|[+-]|[^\\d]+', term)
    if parts[0] in '+-':
        parts[0] += '1'
    if len(parts) == 2:
        return {parts[1]: int(parts[0]) * scale}
    elif len(parts) == 1:
        try:
            return {None: int(parts[0]) * scale}
        except ValueError:
            return {parts[0]: scale}
    else:
        raise Exception('assertion failed')


def combine_term_dicts(a, b):
    common_keys = set(a.keys()).intersection(b.keys())
    common_terms = {k: a[k] + b[k] for k in common_keys}

    def unique_terms(c):
        return {k: v for (k, v) in c.items() if k not in common_keys}
    return {**common_terms, **unique_terms(a), **unique_terms(b)}


def parse_side(side, scale):
    no_ws = re.sub(' ', '', side)
    term_str = re.findall('[+-]?\\d*[^\\d+-]*', no_ws)[0:-1]
    term_lst = [parse_term(t, scale) for t in term_str]
    return reduce(combine_term_dicts, term_lst)


def parse_equation(eq):
    sides = eq.split('=')
    lhs = parse_side(sides[0], 1)
    rhs = parse_side(sides[1], -1)
    return combine_term_dicts(lhs, rhs)


def argmax(lst):
    return [i for i in range(len(lst)) if lst[i] == max(lst)][0]


aug = [[1, -4, 0], [2, -8, 0], [1, 1, 5]]


def gaussian_elimination_inplace(aug):
    n_equations = len(aug)
    n_variables = len(aug[0]) - 1
    for i in range(min(n_variables, n_equations - 1)):
        p = i + argmax([abs(aug[j][i]) for j in range(i, n_equations)])
        if abs(aug[p][i]) < 1e-12:
            raise ValueError('system is singular')
        (aug[i], aug[p]) = (aug[p], aug[i])
        for j in range(i + 1, n_equations):
            beta = aug[j][i] / aug[i][i]
            for k in range(n_variables + 1):
                aug[j][k] -= aug[i][k] * beta


def backsolve(aug):
    n_equations = len(aug)
    n_variables = len(aug[0]) - 1
    sol = [aug[i][n_variables] for i in range(n_variables)]
    for i in reversed(range(n_variables)):
        for j in range(i + 1, n_variables):
            sol[i] -= aug[i][j] * sol[j]
        if abs(aug[i][i]) < 1e-12:
            raise ValueError('system is singular')
        sol[i] /= aug[i][i]
    return sol


def solve(*equations):
    lst = [parse_equation(eq) for eq in equations]
    variables = map(set, map(dict.keys, lst))
    variables = [v for v in reduce(set.union, variables) if v]
    n_variables = len(variables)
    n_equations = len(equations)
    if n_equations < n_variables:
        return None
    aug = [[0] * (n_variables + 1) for i in range(n_equations)]
    for i in range(n_equations):
        for j in range(n_variables):
            aug[i][j] = lst[i].get(variables[j], 0)
        aug[i][n_variables] = -lst[i].get(None, 0)
    try:
        gaussian_elimination_inplace(aug)
        sol = backsolve(aug)
    except ValueError:
        return None
    return {k: v for (k, v) in zip(variables, sol)}

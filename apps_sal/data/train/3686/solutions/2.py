import math


def solve(s: list, mp=0):
    LHS = s.pop(0)
    while len(s) > 0:
        op = s[0]
        p = 1 if op in '+-' else 2
        if p < mp:
            break
        p += 1
        s.pop(0)
        RHS = solve(s, p)
        if op == '+':
            LHS += RHS
        elif op == '-':
            LHS -= RHS
        elif op == '*':
            LHS *= RHS
        elif RHS != 0:
            LHS /= RHS
        else:
            return math.nan
    return LHS


def calculate(s):
    try:
        s = s.replace(' ', '')
    except:
        return False
    dim = len(s)
    if dim == 0:
        return False
    for c in s:
        if not c in '0123456789.+-*/':
            return False
    for i in range(dim - 1):
        if s[i] in '+-*/' and s[i + 1] in '+-*/':
            return False
    exp = []
    i = 0
    for (j, c) in enumerate(s):
        if i == j:
            pass
        elif c in ['+', '-', '*', '/']:
            try:
                exp.append(float(s[i:j]))
            except:
                return False
            exp.append(s[j])
            i = j + 1
    try:
        exp.append(float(s[i:]))
    except:
        return False
    v = solve(exp)
    if math.isnan(v):
        return False
    if float(v) == float(int(v)):
        return int(v)
    return v

import re
from collections import defaultdict

def parse_terms(term, sn):
    d = defaultdict(int)
    for m in re.finditer('([+-]?)\s*(\d*)\s*([a-z]*)', term):
        s, n, v = m.groups()
        if n or v:
            n = sn * (int(n or 1) * (1, -1)[s == '-'])
            d[v or '_'] += n    
    return d

def parse_equations(equations):
    res = []
    for eq in equations:
        a, b = eq.split('=')
        d = parse_terms(a, 1)
        for k, v in parse_terms(b, -1).items():
            d[k] += v
        res.append(d)
    return res

def norm_mat(m, var_pos):
    val = m[var_pos]
    if abs(val) > 1e-8:
        for a in range(len(m)):
            m[a] /= val

def sub_mat(m1, m2, var_pos):
    if non_zero(m1[var_pos]):
        for c, v in enumerate(m2):
            m1[c] -= v

def non_zero(x):
    return abs(x) > 1e-8

def solve(*equations):
    print(equations)
    eqs = parse_equations(equations)
    var = sorted({k for d in eqs for k in d}, reverse = True)
    mat = [[d.get(k, 0) for k in var] for d in eqs]
    num_of_vars = len(var) - 1
    seen = set()
    p = 0
    while p < len(mat):
        var_pos = next(c for c in range(num_of_vars) if non_zero(mat[p][c]) and c not in seen)
        seen.add(var_pos)
        norm_mat(mat[p], var_pos)
        for n in range(p + 1, len(mat)):
            norm_mat(mat[n], var_pos)
            sub_mat(mat[n], mat[p], var_pos)
        mat = [m for m in mat if any(map(non_zero, m))]
        p += 1
    seen.clear()

    d = {}
    while mat:
        el = mat.pop()
        p = next(a for a in range(num_of_vars) if el[a] == 1.0 and a not in d)
        for k, v in d.items():
            el[-1] += el[k] * v
        d[p] = -el[-1]
    
    if len(d) == num_of_vars:
        return {var[k] : v for k, v in d.items()}

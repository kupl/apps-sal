from itertools import combinations


def count_col_triang(a):
    (p, r) = ({}, {})
    for (xy, col) in a:
        p[col] = p.get(col, []) + [xy]
    for k in p:
        r[k] = sum((1 for c in combinations(p[k], 3) if triangle(*c)))
    mx = max(r.values())
    return [len(a), len(p), sum(r.values()), sorted((k for k in r if r[k] == mx)) + [mx] if mx else []]


def triangle(a, b, c):
    return area(*[((p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2) ** 0.5 for (p, q) in [(a, b), (a, c), (b, c)]]) > 0.0


def area(a, b, c):
    s = 0.5 * (a + b + c)
    return round(max(s * ((s - a) * (s - b) * (s - c)), 0.0) ** 0.5, 4)

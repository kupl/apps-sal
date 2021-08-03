import re


def differentiate(equation, point):
    d = {int(p or 1): int({'': 1, '-': -1}.get(n, n)) for n, x, p in re.findall('([-]?\d*)(?:(x)(?:\^(\d+))?)?', equation) if x or p}
    return sum(t * p * point ** (p - 1) for p, t in d.items())

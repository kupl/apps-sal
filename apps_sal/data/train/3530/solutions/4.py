def asterisc_it(n):
    n = x(n)
    h = n[1:]
    return n[0] + ''.join([[e, '*' + e][all((not int(e) % 2, not int(n[i - 1]) % 2))] for i, e in enumerate(h, 1)])


def x(c): return str(c) if not type(c) is list else ''.join(map(str, c))

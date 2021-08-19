from fractions import gcd


def para_to_rect(eqn1, eqn2):
    (a1, b1) = coeff(eqn1, 'x')
    (a2, b2) = coeff(eqn2, 'y')
    A = a2
    B = -a1
    C = b1 * a2 - a1 * b2
    g = gcd(gcd(A, B), C)
    cf = [v // g for v in [A, B, C]]
    if cf[0] < 0:
        cf = [-1 * v for v in cf]
    s = '+' if cf[1] >= 0 else '-'
    cf[1] = abs(cf[1])
    (a, b, c) = ['' if abs(v) == 1 else str(v) for v in cf]
    return '{}x {} {}y = {}'.format(a, s, b, c)


def coeff(eq, v):
    p1 = eq.replace(' ', '').replace(v + '=', '').split('t')
    return list([1 if x == '' else -1 if x == '-' else int(x) for x in p1])

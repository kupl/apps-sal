from math import gcd


def extract(eq):
    (k, b) = eq.split('t')
    k = k[3:].strip()
    k = (int(k) if k != '-' else -1) if k else 1
    b = b.strip()
    b = (-1 if b[0] == '-' else 1) * int(b[1:].strip()) if b else 0
    return (k, b)


def quotient(x):
    return '' if x == 1 else '-' if x == -1 else str(x)


def para_to_rect(eqn1, eqn2):
    (a, b) = extract(eqn1)
    (k, d) = extract(eqn2)
    l = -a
    m = k * b - a * d
    g = gcd(gcd(k, l), m)
    if k * g < 0:
        g = -g
    k //= g
    l //= g
    m //= g
    return f"{quotient(k)}x {'+-'[l < 0]} {quotient(abs(l))}y = {m}"

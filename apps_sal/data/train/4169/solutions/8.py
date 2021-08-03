import re
import math


def para_to_rect(eqn1, eqn2):
    a = re.search(r'(-?\d*)(?=t)', eqn1)
    if a is None:
        a = 1
    else:
        if a.group(0) == '':
            a = 1
        elif a.group(0) == '-':
            a = -1
        else:
            a = int(a.group(0))
    c = re.search(r'(-?\d*)(?=t)', eqn2)
    if c is None:
        c = 1
    else:
        if c.group(0) == '':
            c = 1
        elif c.group(0) == '-':
            c = -1
        else:
            c = int(c.group(0))
    b = re.search(r'[-\+]? \d*\Z', eqn1)
    if b is None:
        b = 0
    else:
        b = int(b.group(0).replace(' ', ''))
    d = re.search(r'[-\+]? \d*\Z', eqn2)
    if b is None:
        d = 0
    else:
        d = int(d.group(0).replace(' ', ''))
    n = (a * c) // math.gcd(a, c)
    k = (-1 if c < 0 else 1)
    x = k * n // a
    y = -k * n // c
    z = k * b * n // a - k * d * n // c
    xp = '' if x == 0 else '{}x'.format('-' if x == - 1 else '' if x == 1 else abs(x))
    yp = '' if y == 0 else '{}{}y'.format(' - ' if y < 0 else ' + ', '' if abs(y) == 1 else abs(y))
    return '{}{} = {}'.format(xp, yp, z)

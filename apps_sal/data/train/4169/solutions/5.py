def gcd(x, y):
    while y:
        (x, y) = (y, x % y)
    return x


def parseeq(s):
    s = s.split()
    a = s[2].replace('t', '')
    if a == '':
        a = 1
    elif a == '-':
        a = -1
    else:
        a = int(a)
    try:
        b = int(s[3] + s[4])
    except:
        b = 0
    return (a, b)


def para_to_rect(eqn1, eqn2):
    (a, b) = parseeq(eqn1)
    (c, d) = parseeq(eqn2)
    e = b * c - a * d
    if c < 0:
        (a, c, e) = (-a, -c, -e)
    g = gcd(a, gcd(abs(c), abs(e)))
    (a, c, e) = (a // g, c // g, e // g)
    sign = '+-'[a > 0]
    if c == 1:
        p1 = ''
    elif c == '-1':
        p1 = '-'
    else:
        p1 = c
    if a == 1:
        p2 = ''
    elif a == -1:
        p2 = ''
    else:
        p2 = abs(a)
    return '{}x {} {}y = {}'.format(p1, sign, p2, e)

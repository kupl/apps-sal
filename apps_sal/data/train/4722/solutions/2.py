def e(p, u=[]):
    if p:
        u += list('0' * (p[0] == '-') + p + ')')
    (a, o, x) = (0, '+', u.pop)
    while o != ')':
        y = x(0)
        c = e(0) if y == '(' else y
        while u[0] not in ')+-*/':
            c += x(0)
        b = float(c)
        a = {'+': a + b, '-': a - b, '*': a * b, '/': a / (b or 1)}[o]
        o = x(0)
    return a

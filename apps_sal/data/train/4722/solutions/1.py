def e(s, t=[], x=0, o='+', m=')*+-/'):
    if s:
        t += list(s.replace(' ', '') + ')')
    while o != ')':
        c = t.pop(0)
        if c == '(':
            c = e(0)
        while t[0] not in m:
            c += t.pop(0)
        c = float(c)
        x = {'*': x * c, '+': x + c, '-': x - c, '/': x / c}[o]
        o = t.pop(0)
    return x

def e(s, l=0, n=0, f='+'):
    if s:
        l = [c for c in s + ')'if' ' != c]
    while f != ')':
        p = l.pop
        m = p(0)
        if m == '(':
            m = e(0, l)
        while l[0]not in '+-*/)':
            m += p(0)
        m = float(m)
        n = {'+': n + m, '-': n - m, '*': n * m, '/': n / (m or 1)}[f]
        f = p(0)
    return n

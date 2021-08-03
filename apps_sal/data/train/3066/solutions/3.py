def solve(s, p=1, q=1, Q=[], z=''):
    for c in s:
        if c == '+':
            p = 1
        elif c == '-':
            p = -1
        elif c == '(':
            q *= p
            Q += [p]
            p = 1
        elif c == ')':
            q *= Q.pop()
            p = 1
        else:
            z += '-+'[p * q > 0] + c
    return z.strip('+')

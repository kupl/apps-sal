def solve(eq):
    leq = eq.replace('*', ' * ').replace('/', ' / ').replace('+', ' + ').replace('-', ' - ').split(' ')
    out = ''.join(leq[::-1])
    return out

def solve(eq):
    s = eq.replace('+', ' + ').replace('-', ' - ').replace('/', ' / ').replace('*', ' * ')
    return ''.join(s.split()[::-1])

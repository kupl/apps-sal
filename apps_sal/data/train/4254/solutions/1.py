def solve(eq):
    #
    # implemantation takes advantage of abscence of spaces
    #
    leq = (eq.replace('*', ' * ')
             .replace('/', ' / ')
             .replace('+', ' + ')
             .replace('-', ' - ')
             .split(' '))

    out = ''.join(leq[::-1])

    return out

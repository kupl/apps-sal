def solve(eq):
    eqnLen = len(eq)

    revEqn = ''
    token = ''
    i = 0

    while i < eqnLen:
        token = eq[i]
        while (i + 1 < eqnLen) and (token.isdigit()) and (eq[i + 1].isdigit()):
            i += 1
            token += eq[i]
        revEqn = token + revEqn
        i += 1

    return revEqn

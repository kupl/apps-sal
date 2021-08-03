def solve(eq):
    eqnLen = len(eq)

    revEqn = ''
    token = ''  # this will be a sigle alpha, or an entire number
    i = 0

    # build the reversed eqation (care regarding the numbers)
    while i < eqnLen:
        token = eq[i]
        # if we have hit a digit (and the next char is a digit) and we are not out of bounds
        # then we need to gobble up the entire number in non-reversed order
        # e.g. 849 should be the token '849' not '948'
        while (i + 1 < eqnLen) and (token.isdigit()) and (eq[i + 1].isdigit()):
            i += 1
            token += eq[i]
        revEqn = token + revEqn  # push token ontop of existing equation
        i += 1

    return revEqn
# end solve function

def polynomialize(roots):
    space_sign_space = lambda c: ' + ' if 0 < c else ' - '
    space_sign_space_num = lambda c: space_sign_space(c)  + (str(abs(c)) if abs(c) != 1 else '')
    max_power = len(roots)
    # Calculate coefficients
    coefs = [1, -roots[0]]
    if max_power > 1:
        for r in roots[1:]:
            coefs = [1,] + [c[0]-r*c[1] for c in zip(coefs[1:], coefs[:-1])] + [-r*coefs[-1],]
    # Construct equation (first line, separately as it needs no leading +)
    eq = 'x' + ('^' + str(max_power) if max_power > 1 else '')
    power = max_power
    # Loop for x^(max_power -1) up to x^2 if it exists
    for c in coefs[1:-2]:
        power -= 1
        if c == 0:
            continue
        eq += space_sign_space_num(c)
        eq += 'x^' + str(power)
    # Coefficient for x
    if (max_power > 1) and coefs[-2] != 0:
        eq += space_sign_space_num(coefs[-2])
        eq += 'x'
    # Coefficient for const
    if coefs[-1] != 0:
        eq += space_sign_space(coefs[-1]) + str(abs(coefs[-1]))
    eq += ' = 0'
    return eq

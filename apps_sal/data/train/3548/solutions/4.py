def polynomialize(roots):
    def space_sign_space(c): return ' + ' if 0 < c else ' - '
    def space_sign_space_num(c): return space_sign_space(c) + (str(abs(c)) if abs(c) != 1 else '')
    max_power = len(roots)
    coefs = [1, -roots[0]]
    if max_power > 1:
        for r in roots[1:]:
            coefs = [1, ] + [c[0] - r * c[1] for c in zip(coefs[1:], coefs[:-1])] + [-r * coefs[-1], ]
    eq = 'x' + ('^' + str(max_power) if max_power > 1 else '')
    power = max_power
    for c in coefs[1:-2]:
        power -= 1
        if c == 0:
            continue
        eq += space_sign_space_num(c)
        eq += 'x^' + str(power)
    if (max_power > 1) and coefs[-2] != 0:
        eq += space_sign_space_num(coefs[-2])
        eq += 'x'
    if coefs[-1] != 0:
        eq += space_sign_space(coefs[-1]) + str(abs(coefs[-1]))
    eq += ' = 0'
    return eq

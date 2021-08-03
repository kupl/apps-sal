def greek_comparator(lhs, rhs):
    greek_alphabet = (
        'alpha', 'beta', 'gamma', 'delta', 'epsilon', 'zeta',
        'eta', 'theta', 'iota', 'kappa', 'lambda', 'mu',
        'nu', 'xi', 'omicron', 'pi', 'rho', 'sigma',
        'tau', 'upsilon', 'phi', 'chi', 'psi', 'omega')

    lhs = greek_alphabet.index(lhs)
    rhs = greek_alphabet.index(rhs)
    if lhs < rhs:
        return -1
    elif lhs == rhs:
        return 0
    elif lhs > rhs:
        return 1

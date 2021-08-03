def greek_comparator(lhs, rhs):
    greek_alphabet = (
        'alpha', 'beta', 'gamma', 'delta', 'epsilon', 'zeta',
        'eta', 'theta', 'iota', 'kappa', 'lambda', 'mu',
        'nu', 'xi', 'omicron', 'pi', 'rho', 'sigma',
        'tau', 'upsilon', 'phi', 'chi', 'psi', 'omega')
    a, b = greek_alphabet.index(lhs), greek_alphabet.index(rhs)
    if a < b:
        return a - b
    return a + b if a > b else 0

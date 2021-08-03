def greek_comparator(lhs, rhs):
    greek = (
        'alpha', 'beta', 'gamma', 'delta', 'epsilon', 'zeta',
        'eta', 'theta', 'iota', 'kappa', 'lambda', 'mu',
        'nu', 'xi', 'omicron', 'pi', 'rho', 'sigma',
        'tau', 'upsilon', 'phi', 'chi', 'psi', 'omega')

    return greek.index(lhs) - greek.index(rhs)

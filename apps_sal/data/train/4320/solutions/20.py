greek_alphabet = ('alpha', 'beta', 'gamma', 'delta', 'epsilon', 'zeta', 'eta', 'theta', 'iota', 'kappa', 'lambda', 'mu', 'nu', 'xi', 'omicron', 'pi', 'rho', 'sigma', 'tau', 'upsilon', 'phi', 'chi', 'psi', 'omega')


def greek_comparator(lhs, rhs):
    (index_lhs, index_rhs) = map(greek_alphabet.index, (lhs, rhs))
    return int(index_lhs > index_rhs) or -int(index_lhs < index_rhs)

def greek_comparator(lhs, rhs):
    greek_alphabet = ['alpha', 'beta', 'gamma', 'delta', 'epsilon', 'zeta', 
    'eta', 'theta', 'iota', 'kappa', 'lambda', 'mu', 
    'nu', 'xi', 'omicron', 'pi', 'rho', 'sigma',
    'tau', 'upsilon', 'phi', 'chi', 'psi', 'omega']
    a = greek_alphabet.index(lhs)
    b = greek_alphabet.index(rhs)
    c=a-b
    return c

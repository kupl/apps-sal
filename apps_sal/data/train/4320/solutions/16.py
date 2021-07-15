def greek_comparator(lhs, rhs):
    greek_alphabet = (
    'alpha', 'beta', 'gamma', 'delta', 'epsilon', 'zeta', 
    'eta', 'theta', 'iota', 'kappa', 'lambda', 'mu', 
    'nu', 'xi', 'omicron', 'pi', 'rho', 'sigma',
    'tau', 'upsilon', 'phi', 'chi', 'psi', 'omega')
    
    return 1 if greek_alphabet.index(lhs) > greek_alphabet.index(rhs) else \
           0 if greek_alphabet.index(lhs) == greek_alphabet.index(rhs) else \
           -1

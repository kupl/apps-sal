def greek_comparator(lhs, rhs):
    # the tuple greek_alphabet is defined in the nonlocal namespace
    greek_alphabet = (
    'alpha', 'beta', 'gamma', 'delta', 'epsilon', 'zeta', 
    'eta', 'theta', 'iota', 'kappa', 'lambda', 'mu', 
    'nu', 'xi', 'omicron', 'pi', 'rho', 'sigma',
    'tau', 'upsilon', 'phi', 'chi', 'psi', 'omega')
    
    if greek_alphabet.index(lhs) > greek_alphabet.index(rhs):
        return greek_alphabet.index(lhs) - greek_alphabet.index(rhs)
    elif greek_alphabet.index(lhs) < greek_alphabet.index(rhs) :
        return greek_alphabet.index(lhs) - greek_alphabet.index(rhs)
    return 0

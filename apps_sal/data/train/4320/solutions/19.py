def greek_comparator(l, r):
    greek_alphabet = (
    'alpha', 'beta', 'gamma', 'delta', 'epsilon', 'zeta', 
    'eta', 'theta', 'iota', 'kappa', 'lambda', 'mu', 
    'nu', 'xi', 'omicron', 'pi', 'rho', 'sigma',
    'tau', 'upsilon', 'phi', 'chi', 'psi', 'omega')
    if greek_alphabet.index(l) < greek_alphabet.index(r) : 
        return -1
    elif greek_alphabet.index(l) == greek_alphabet.index(r) :
        return 0
    return 1


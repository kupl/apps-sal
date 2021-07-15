def greek_comparator(lhs, rhs):
    g = (
    'alpha', 'beta', 'gamma', 'delta', 'epsilon', 'zeta', 
    'eta', 'theta', 'iota', 'kappa', 'lambda', 'mu', 
    'nu', 'xi', 'omicron', 'pi', 'rho', 'sigma',
    'tau', 'upsilon', 'phi', 'chi', 'psi', 'omega')
    a = g.index(lhs)
    b = g.index(rhs)
    if a == b:
        return 0
    if a > b:
        return 1
    if a < b:
        return -1
    


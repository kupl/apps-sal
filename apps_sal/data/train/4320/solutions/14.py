def greek_comparator(lhs, rhs):
    ga = [
    'alpha', 'beta', 'gamma', 'delta', 'epsilon', 'zeta', 
    'eta', 'theta', 'iota', 'kappa', 'lambda', 'mu', 
    'nu', 'xi', 'omicron', 'pi', 'rho', 'sigma',
    'tau', 'upsilon', 'phi', 'chi', 'psi', 'omega']
    return -1 if ga.index(lhs)<ga.index(rhs) else 0 if ga.index(lhs)==ga.index(rhs) else 1

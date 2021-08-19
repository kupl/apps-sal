def greek_comparator(lhs, rhs):
    greek_alphabet = ['alpha', 'beta', 'gamma', 'delta', 'epsilon', 'zeta', 'eta', 'theta', 'iota', 'kappa', 'lambda', 'mu', 'nu', 'xi', 'omicron', 'pi', 'rho', 'sigma', 'tau', 'upsilon', 'phi', 'chi', 'psi', 'omega']
    l = len(greek_alphabet)
    k = 0
    v = 0
    i = 0
    for i in range(l):
        if lhs == greek_alphabet[i]:
            k = i
    i += 1
    i = 0
    for i in range(l):
        if rhs == greek_alphabet[i]:
            v = i
    i += 1
    b = k - v
    return b

def greek_comparator(lhs, rhs):
    # the tuple greek_alphabet is defined in the nonlocal namespace
    greek_alphabet = (
        'alpha', 'beta', 'gamma', 'delta', 'epsilon', 'zeta',
        'eta', 'theta', 'iota', 'kappa', 'lambda', 'mu',
        'nu', 'xi', 'omicron', 'pi', 'rho', 'sigma',
        'tau', 'upsilon', 'phi', 'chi', 'psi', 'omega')

    dict_old = dict(enumerate(greek_alphabet))
    dict_new = {value: key for key, value in dict_old.items()}

    if dict_new[lhs] < dict_new[rhs]:
        return -1
    elif dict_new[lhs] == dict_new[rhs]:
        return 0
    else:
        return +1

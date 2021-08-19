def greek_comparator(lhs, rhs):
    greek_alphabet = {'alpha': 1, 'beta': 2, 'gamma': 3, 'delta': 4, 'epsilon': 5, 'zeta': 6, 'eta': 7, 'theta': 8, 'iota': 9, 'kappa': 10, 'lambda': 11, 'mu': 12, 'nu': 13, 'xi': 14, 'omicron': 15, 'pi': 16, 'rho': 17, 'sigma': 18, 'tau': 19, 'upsilon': 20, 'phi': 21, 'chi': 22, 'psi': 23, 'omega': 24}
    a = greek_alphabet.get(lhs) - greek_alphabet.get(rhs)
    return a

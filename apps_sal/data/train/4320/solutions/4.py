greek_alphabet = ('alpha', 
'beta', 
'gamma', 
'delta', 
'epsilon', 
'zeta', 
'eta', 
'theta', 
'iota', 
'kappa', 
'lambda', 
'mu', 
'nu', 
'xi', 
'omicron', 
'pi', 
'rho', 
'sigma', 
'tau', 
'upsilon', 
'phi', 
'chi', 
'psi', 
'omega')

def greek_comparator(lhs, rhs):
    x = greek_alphabet.index(lhs)
    y = greek_alphabet.index(rhs)
    if x < y:
        return -1
    elif x == y:
        return 0
    else:
        return 1

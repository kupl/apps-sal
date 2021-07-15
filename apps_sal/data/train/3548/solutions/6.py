from functools import reduce

def toTerm(coef, power):
    if not coef or coef == 0: return ''
    if power == 0: 
        p = ''
    elif power == 1:
        p = 'x'
    else:
        p = 'x^' + str(power)
    
    term = ('' if abs(coef) == 1 and power > 0 else str(abs(coef))) + p
    return (' - ' if coef < 0 else ' + ') + str(term) if term else ''

def co2poly(coefs):
    terms = [toTerm(c, i) for i, c in enumerate(coefs)]
    terms.reverse()
    t = ''.join(terms)
    return (t[3:] if t.startswith(' +') else t[1:]) + ' = 0'

def toCoefs(coefs, root):
    return [ n * -root + c for (c, n) in zip([0] + coefs, coefs + [0]) ]

def polynomialize(roots):
    coefs = reduce(toCoefs, roots, [1])
    return co2poly(coefs)


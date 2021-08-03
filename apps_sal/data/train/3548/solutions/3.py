import numpy as np


def string(v): return "" if not v else "x" if v == 1 else f"x^{v}"


def coefficients(roots):
    coeffs = [1, -roots.pop()]
    while roots:
        coeffs.append(0)
        r = roots.pop()
        for i in reversed(range(1, len(coeffs))):
            coeffs[i] -= r * coeffs[i - 1]
    return coeffs

# numpy.poly1d gives slighty different coeffs


def polynomialize(roots):
    #coeffs = list(map(int, np.poly1d(roots, True)))
    coeffs = coefficients(roots)
    z = zip(reversed(range(len(coeffs))), coeffs)
    res = [string(next(z)[0])]
    res.extend(f" {'-+'[b > 0]} {(abs(b), '')[a and abs(b) == 1]}{string(a)}" for a, b in z if b)
    res.append(" = 0")
    return ''.join(res)

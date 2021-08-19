from math import log


def decompose(n):
    """
    Given integer n, finds the coefficient and exponent of 2 decomposition
    (c, p) such that c * 2^p == n when c, p are both integers
    """
    for p in range(int(log(n, 2)), -1, -1):
        c = n / 2 ** p
        if c == int(c):
            c = int(c)
            return (c, p)


def sharkovsky(a, b):
    """
    Given a, b determine if a precedes b in a Sharkovsky sequence.

    Any natural number can be decomposed into a position in the table (k \\in \\mathbb{N}):

         3.2^0           5.2^0           7.2^0  ...  (2(k-1)+1).2^0  (2k+1).2^0    ...
         3.2^1           5.2^1           7.2^1  ...  (2(k-1)+1).2^1  (2k+1).2^1    ...
         3.2^2           5.2^2           7.2^2  ...  (2(k-1)+1).2^2  (2k+1).2^2    ...
         3.2^3           5.2^3           7.2^3  ...  (2(k-1)+1).2^3  (2k+1).2^3    ...
           ...             ...             ...  ...             ...         ...    ...
    1.2^(2k+1)  1.2^(2(k-1)+1)  1.2^(2(k-2)+1)  ...           2.2^2       1.2^1  1.2^0

    Reading the table left to right, top to bottom gives the Sharkovsky sequence
    """
    (coef_a, exp_a) = decompose(a)
    (coef_b, exp_b) = decompose(b)
    if coef_a == 1 and coef_b == 1:
        return exp_b < exp_a
    if coef_a == 1 or coef_b == 1:
        return coef_b == 1
    if exp_a != exp_b:
        return exp_a < exp_b
    if exp_a == exp_b:
        return coef_a < coef_b
    return False

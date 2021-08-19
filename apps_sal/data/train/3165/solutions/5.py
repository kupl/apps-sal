from math import floor, log
'\nSee: https://oeis.org/A139250\nFormulas:\n  Let n = msb(n) + j where msb(n) = A053644(n)\n  let a(0) = 0. \n  Then a(n) = (2 * msb(n)^2 + 1) / 3 + 2 * a(j) + a(j + 1) - 1\n    - David A. Corneth, Mar 26 2015\n    \nNote: A053644(n) is the sequence of largest power of 2 <= n\nSee: https://oeis.org/A053644\n'


def toothpick(n):
    """Returns number of picks required for n rounds of the toothpick sequence"""
    if n < 2:
        return n
    msb_n = 2 ** floor(log(n, 2))
    j = n - msb_n
    return (2 * msb_n ** 2 + 1) / 3 + 2 * toothpick(j) + toothpick(j + 1) - 1

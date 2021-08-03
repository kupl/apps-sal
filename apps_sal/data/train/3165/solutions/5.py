from math import floor, log

"""
See: https://oeis.org/A139250
Formulas:
  Let n = msb(n) + j where msb(n) = A053644(n)
  let a(0) = 0. 
  Then a(n) = (2 * msb(n)^2 + 1) / 3 + 2 * a(j) + a(j + 1) - 1
    - David A. Corneth, Mar 26 2015
    
Note: A053644(n) is the sequence of largest power of 2 <= n
See: https://oeis.org/A053644
"""


def toothpick(n):
    """Returns number of picks required for n rounds of the toothpick sequence"""
    if n < 2:
        return n

    msb_n = 2 ** floor(log(n, 2))
    j = n - msb_n
    return (2 * msb_n ** 2 + 1) / 3 + 2 * toothpick(j) + toothpick(j + 1) - 1

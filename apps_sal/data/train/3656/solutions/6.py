from fractions import Fraction
import math


def decompose(n):

    if n == '0':
        return []

    refFrac = Fraction(n)
    if refFrac.numerator == refFrac.denominator:
        return ['1']
    elif refFrac.denominator == 1:
        return [str(refFrac.numerator)]

    final_tab = []
    while(refFrac.numerator != 0):
        denom = math.ceil(refFrac.denominator / refFrac.numerator)
        next = Fraction(1, denom)
        final_tab.append(next)
        refFrac -= next

    return [str(frac) for frac in final_tab]

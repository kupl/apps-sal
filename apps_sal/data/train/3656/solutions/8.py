from fractions import Fraction
import sys
from math import floor, ceil


class EgyptianFraction(Fraction):
    def decompose(self, rst=None):
        if rst is None:
            rst = []

        # stop condition
        if self == 0:
            return rst
        elif self.numerator == 1 or self.denominator == 1:
            rst.append(Fraction(self))
            return rst

        # greedy search
        if self > 1:
            frac = Fraction(floor(self))
        else:
            frac = Fraction(1, ceil(1 / self))
        rst.append(frac)
        return EgyptianFraction(self - frac).decompose(rst)


def decompose(n):
    rst = EgyptianFraction(n).decompose()
    return [str(i) for i in rst]

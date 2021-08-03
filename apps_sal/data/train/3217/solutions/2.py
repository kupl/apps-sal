from fractions import Fraction


def sum_fracts(lst):
    if lst:
        ret = sum(map(lambda l: Fraction(*l), lst))
        return [ret.numerator, ret.denominator] if ret.denominator != 1 else ret.numerator

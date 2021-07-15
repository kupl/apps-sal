from functools import reduce


def disjunction(operands, is_exclusive):
    return reduce(bool.__xor__ if is_exclusive else bool.__or__, operands)

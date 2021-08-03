from functools import reduce


def disjunction(operands, is_exclusive):
    op = int.__xor__ if is_exclusive else int.__or__
    return reduce(op, operands)

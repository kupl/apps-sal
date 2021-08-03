from decimal import *


def find_nb(m):
    getcontext().prec = 24
    squareRootM = Decimal(m).sqrt()
    squareRootDelta = Decimal(1 + 8 * squareRootM).sqrt()
    num = (squareRootDelta - 1) / 2
    return num if num % 1 == 0 else -1

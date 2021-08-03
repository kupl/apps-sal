import operator
from functools import reduce


def share_price(invested, changes):
    multipliers = (1.0 + c / 100.0 for c in changes)
    product = reduce(operator.mul, multipliers, 1.0)
    return '%.2f' % (invested * product)

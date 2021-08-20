from functools import reduce


def sum_prod(strexpression):
    to_sum = [expr.split('*') for expr in strexpression.split('+')]
    total = sum((reduce(lambda result, y: result * float(y), product_, 1.0) for product_ in to_sum))
    return f'{total:.5e}'

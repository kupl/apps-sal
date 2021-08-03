from itertools import product, zip_longest


def operator_insertor(n):
    inserts = []
    for ops in product(('+', '-', ''), repeat=8):
        expression = ''.join(map(''.join, zip_longest('123456789', ops, fillvalue='')))
        if eval(expression) == n:
            inserts.append(len(expression) - 9)
    return min(inserts, default=None)

from itertools import product


def operator_insertor(n):
    result = []
    for ops in product(['+', '-', ''], repeat=8):
        expression = ''.join((a + b for (a, b) in zip('123456789', list(ops) + [''])))
        res = eval(expression)
        if res == n:
            result.append(len(expression) - 9)
    return min(result, default=None)

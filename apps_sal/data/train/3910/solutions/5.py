from itertools import product


def operator_insertor(n):
    def equation(ops): return ''.join(f'{a}{b}' for a, b in enumerate(ops + ('',), 1))
    candidates = product(('', '+', '-'), repeat=8)
    matches = (len(''.join(ops)) for ops in candidates if eval(equation(ops)) == n)
    return min(matches, default=None)

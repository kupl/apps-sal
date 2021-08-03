from itertools import product


def is_divisible_by_6(s):
    return [''.join(p) for p in product(*list('0123456789' if c == '*' else c for c in s)) if int(''.join(p)) % 6 == 0]

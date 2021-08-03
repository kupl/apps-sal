from functools import reduce


def sum_of_threes(n):
    return ['Impossible' if r else '+'.join(xs) for r, xs in [reduce(lambda v, x: (v[0] - 3**x, v[1] + [f'3^{x}']) if v[0] >= 3**x else v, range(34)[::-1], (n, []))]][0]

import operator
from itertools import product, permutations


def mydiv(n, d):
    return n / d if d != 0 else 9999999


syms = [operator.add, operator.sub, operator.mul, mydiv]
op = {sym: ch for (sym, ch) in zip(syms, '+-*/')}


def solve24(nums):
    for (x, y, z) in product(syms, repeat=3):
        for (a, b, c, d) in permutations(nums):
            if round(x(y(a, b), z(c, d)), 5) == 24:
                return f'({a} {op[y]} {b}) {op[x]} ({c} {op[z]} {d})'
            elif round(x(a, y(b, z(c, d))), 5) == 24:
                return f'{a} {op[x]} ({b} {op[y]} ({c} {op[z]} {d}))'
            elif round(x(y(z(c, d), b), a), 5) == 24:
                return f'(({c} {op[z]} {d}) {op[y]} {b}) {op[x]} {a}'
            elif round(x(y(b, z(c, d)), a), 5) == 24:
                return f'({b} {op[y]} ({c} {op[z]} {d})) {op[x]} {a}'
    return "It's not possible!"


def equal_to_24(a, b, c, d):
    nums = []
    nums.append(a)
    nums.append(b)
    nums.append(c)
    nums.append(d)
    return solve24(nums)

from fractions import Fraction as F
cache = {}


def divisors(n):
    result = cache.get(n)
    if result is not None:
        return result
    if n < 2:
        return [1] if n == 1 else []
    result = set([1, n])
    for i in range(2, n // 2):
        if n % i == 0:
            result.add(i)
            result.add(n // i)
    cache[n] = result
    return result


def solve(a, b):
    print(f'a: {a}, b: {b}')
    vals = {}
    for n in range(max(a, 1), b):
        r = F(sum(divisors(n)), n)
        vals.setdefault(r, []).append(n)
    result = 0
    for (k, v) in vals.items():
        if len(v) >= 2:
            result += v[0]
    return result

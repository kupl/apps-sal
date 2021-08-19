def primeFactors(n):
    s = {k for k in range(2, int(abs(n) ** 0.5) + 1) for i in range(2, int(abs(k) ** 0.5) + 1) if k % i == 0}
    p = [j for j in range(2, int(abs(n) ** 0.5) + 1) if j not in s]
    z = [i for i in f_idx(n, p) if i != 1]
    return ''.join([f'({i}**{z.count(i)})' if z.count(i) > 1 else f'({i})' for i in sorted(set(z))])


def f_idx(n, p):
    from functools import reduce
    e = list(filter(lambda t: n % t == 0, p))
    a = reduce(lambda x, y: x * y, e) if e != [] else 1
    return e + [n] if a == 1 else e + f_idx(n // a, e)

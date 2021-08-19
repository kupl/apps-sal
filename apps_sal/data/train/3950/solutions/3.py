from itertools import combinations


def pwrdivs(s):
    return divisors(sum((sum((int(''.join(c)) for c in combinations(s, k))) for k in range(1, len(s) + 1))))


def strdivs(s):
    return divisors(sum((sum((int(s[i:i + k]) for i in range(len(s) - k + 1))) for k in range(1, len(s) + 1))))


def find_int_inrange(a, b):
    d = {k: len(pwrdivs(str(k)) & strdivs(str(k))) for k in range(a, b + 1)}
    mx = max(d.values())
    return [mx] + [k for k in d if d[k] == mx]


def divisors(n):
    (f, d) = ([], 2)
    while d * d <= n:
        while n % d == 0:
            (f, n) = (f + [d], n // d)
        d += 1
    if n > 1:
        f.append(n)
    (s, f) = (set(), sorted(f))
    [[s.add(c) for c in combinations(f, k)] for k in range(1, len(f))]
    return s

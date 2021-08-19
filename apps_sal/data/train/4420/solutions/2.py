from bisect import bisect_left, bisect_right


def spf(n):
    result = 0
    nd = 0
    while n % 2 == 0:
        result += 2
        nd += 1
        n //= 2
    d = 3
    while n > 1:
        while n % d == 0:
            result += d
            n //= d
            nd += 1
        d += 2
    return n + 1 if nd == 1 else (result or n + 1)  # nd == 1 -> prime


xs = [x for x in range(1, 20001) if x % spf(x) == 0]


def mult_primefactor_sum(a, b):
    i = bisect_left(xs, a)
    j = bisect_right(xs, b)
    return xs[i:j]

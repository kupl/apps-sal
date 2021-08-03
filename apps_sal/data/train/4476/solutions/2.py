from bisect import bisect_right, bisect_left
import itertools
compress = itertools.compress


def prime(n):
    if n < 2:
        return []
    r = [False, True] * (n // 2) + [True]
    r[1], r[2] = False, True
    for i in range(3, int(1 + n**0.5), 2):
        if r[i]:
            r[i * i::2 * i] = [False] * int((n + 2 * i - 1 - i * i) / (2 * i))
    r = list(compress(list(range(len(r))), r))
    if r[-1] % 2 == 0:
        r.pop()
    return r


primes = prime(5 * 10**6)


def even(n):
    even_count = 0
    while n > 0:
        rem = n % 10
        if not rem % 2:
            even_count += 1
        n //= 10
    return even_count


def f(n):
    n -= 1
    upper_bound = bisect_right(primes, n)
    best = -1
    bestCount = 0
    for i in reversed(list(range(0, upper_bound))):
        if len(str(primes[i])) <= bestCount:
            break
        count = even(primes[i])
        if bestCount < count:
            best = primes[i]
            bestCount = count
        elif bestCount == count:
            if primes[i] > best:
                best = primes[i]
                bestCount = count
    return best

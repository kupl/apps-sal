from itertools import compress


def sieve(n):
    n += 1
    r = [False, True] * (n // 2) + [True]
    r[1] = False
    r[2] = True
    for i in range(3, int(n ** 0.5) + 1, 2):
        if r[i]:
            r[i * i::2 * i] = [False] * ((n + 2 * i - 1 - i * i) // (2 * i))
    r = list(compress(list(range(len(r))), r))
    if r[-1] % 2 == 0:
        return r[:-1]
    return r


def test(num):
    num = str(num)
    for i in num:
        if int(i) in (2, 3, 5, 7):
            return False
    return True


primes = set(sieve(10 ** 6))
res = []
for i in range(1, 10 ** 6):
    if i not in primes and test(i):
        res.append(i)


def solve(n):
    return res[n]

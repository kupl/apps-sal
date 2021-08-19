a = [1] * 20000
a[0] = a[1] = 0
for i in range(2, 20000):
    if a[i]:
        for j in range(i ** 2, 20000, i):
            a[j] = 0
a = [i for (i, x) in enumerate(a) if x]


def ds_multof_pfs(a, b):
    return [i for i in range(a, b + 1) if not divisors(i) % primes(i)]


def divisors(n):
    r = 0
    for i in range(1, int(n ** 0.5) + 1):
        if not n % i:
            r += i
            if i * i != n:
                r += n // i
    return r


def primes(n):
    r = 0
    for x in a:
        while not n % x:
            r += x
            n //= x
        if n == 1:
            return r

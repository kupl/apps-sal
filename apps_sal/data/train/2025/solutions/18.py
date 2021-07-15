def primes(n):
    sieve = set(range(3, n + 1, 2))
    if n >= 2:
        sieve.add(2)
    for i in range(3, int(n ** 0.5) + 1, 2):
        if i in sieve:
            sieve -= set(range(2 * i, n + 1, i))
    return sieve


n = int(input())
res = []
for i in primes(n):
    k = i
    while k <= n:
        res.append(str(k))
        k *= i

print(len(res))
print(' '.join(res))

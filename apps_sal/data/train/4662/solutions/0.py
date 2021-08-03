n, forbid = 100000, set("2357")
sieve, notPrimes = [0] * (n + 1), [1]
for i in range(2, n + 1):
    if sieve[i]:
        if not (forbid & set(str(i))):
            notPrimes.append(i)
    else:
        for j in range(i**2, n + 1, i):
            sieve[j] = 1


def solve(n): return notPrimes[n]

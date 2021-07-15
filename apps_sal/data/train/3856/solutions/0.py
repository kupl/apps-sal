n = 500000
sieve, PRIMES = [0]*(n//2+1), [0,2]
for i in range(3, n+1, 2):
    if not sieve[i//2]:
        PRIMES.append(i)
        for j in range(i**2, n+1, i*2): sieve[j//2] = 1

DOMINANTS = []
for p in PRIMES:
    if p >= len(PRIMES): break
    DOMINANTS.append(PRIMES[p])

def solve(a,b):
    return sum(p for p in DOMINANTS if a <= p <= b)

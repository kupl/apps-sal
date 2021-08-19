limit = 50000
sieve = [0] * 2 + list(range(2, limit))
for i in range(2, limit):
    for j in range(i * i, limit, i):
        sieve[j] = 0
primes = {i for i in sieve if i}
(p, i, li) = (['2', '3', '5', '7'], 0, [])
while len(li) <= 3000:
    if i and all((k not in p for k in str(i))) and (i not in primes):
        li.append(i)
    i += 1


def solve(n):
    return li[n]

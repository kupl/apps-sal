def sieve(n):
    l = [True for i in range(n + 1)]
    p = 2
    while(p * p < n):
        if l[p]:
            for i in range(p * p, n + 1, p):
                l[i] = False
        p += 1
    primes = []
    for i in range(2, n):
        if l[i]:
            primes.append(i)
    return primes


sums = [0] * (10001)
p = sieve(10001)

for i in p:
    for j in p:
        if i + (2 * j) <= 10000:
            sums[i + (2 * j)] += 1

t = int(input())
while t:
    n = int(input())
    print(sums[n])
    t -= 1

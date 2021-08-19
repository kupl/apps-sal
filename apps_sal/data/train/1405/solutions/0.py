from bisect import bisect
n = 32000


def primeSeive(n):
    prime = [True for i in range(n + 1)]
    primes = []
    p = 2
    while p * p <= n:
        if prime[p] == True:
            for i in range(p * 2, n + 1, p):
                prime[i] = False
        p += 1
    prime[0] = False
    prime[1] = False
    for p in range(n + 1):
        if prime[p]:
            primes.append(p)
    return primes


arr = primeSeive(n)
fin = []
for i in arr:
    fin.append(pow(i, 4))
for _ in range(int(input())):
    n = int(input())
    print(bisect(fin, n))

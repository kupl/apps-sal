primes = {}


def SieveOfEratosthenes(n):
    prime = [True for i in range(n + 1)]
    p = 2
    while p * p <= n:
        if prime[p] == True:
            for i in range(p * p, n + 1, p):
                prime[i] = False
        p += 1
    for p in range(2, n + 1):
        if prime[p]:
            primes[p] = 1


SieveOfEratosthenes(20000)
factors = {1: 2, 2: 3}
for i in range(3, 15000):
    if i in primes:
        factors[i * i] = 1
    else:
        factors[i * i] = 2
t = int(input())
for case in range(t):
    (n, k1, k2) = list([int(x) for x in input().split()])
    (p1, p2, p3, p4) = list([int(x) for x in input().split()])
    costs = [0, p1, p2, p3, p4]
    cost = 0
    numbers_to_remove = 0
    for number in factors:
        if number >= k1 and number <= k2:
            cost = cost + costs[factors[number]]
            numbers_to_remove += 1
    cost = cost + (k2 - k1 + 1 - numbers_to_remove) * costs[3] % 100000007
    print(cost % 100000007)

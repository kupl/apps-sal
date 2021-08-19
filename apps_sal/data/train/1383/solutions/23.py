primes = {}


def SieveOfEratosthenes(n):

    prime = [True for i in range(n + 1)]
    p = 2
    while (p * p <= n):

        if (prime[p] == True):

            # Update all multiples of p
            for i in range(p * p, n + 1, p):
                prime[i] = False
        p += 1

    # Print all prime numbers
    for p in range(2, n + 1):
        if prime[p]:
            primes[p] = 1


t = int(input())
SieveOfEratosthenes(10000)
factors = {1: 2, 2: 3}

for i in range(3, 5000):
    if i in primes:
        factors[i * i] = 1
    else:
        factors[i * i] = 2

for case in range(t):
    n, k1, k2 = list([int(x) for x in input().split()])
    p1, p2, p3, p4 = list([int(x) for x in input().split()])
    costs = [0, p1, p2, p3, p4]
    cost = 0
    for i in range(k1, k2 + 1):
        if i in factors:
            cost += costs[factors[i]]
        else:
            cost += costs[3]
    print(cost)

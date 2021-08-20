def calcPrimes(tot):
    fin = []
    primes = [1] * (tot + 1)
    start = 2
    while start < tot + 1:
        fin.append(start)
        for i in range(2 * start, tot + 1, start):
            primes[i] = 0
        start += 1
        while start < len(primes) and primes[start] == 0:
            start += 1
    return fin


def solve(tot, primes, primeSet):
    pairs = 0
    for i in primes:
        if (tot - i) % 2 == 0 and (tot - i) // 2 in primeSet:
            pairs += 1
        if tot - 2 * i in primeSet:
            pairs += 1
    print(pairs // 2)


primes = calcPrimes(10 ** 4 + 5)
count = [0] * (10 ** 4 + 5)
for i in primes:
    for j in primes:
        if i + 2 * j < len(count):
            count[i + 2 * j] += 1
n = int(input())
for _ in range(n):
    print(count[int(input())])

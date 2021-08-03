N = (10 ** 6 + 10)


def sieve():
    primes = [0, 0] + [1] * N
    sums = 0
    for i in range(2, N):
        if primes[i]:
            for j in range(i * i, N, i):
                primes[j] = 0
    prime_sums = [0] * N
    now = 0
    for i in range(2, N):
        if primes[i]:
            now += i
        prime_sums[i] = now
    return prime_sums


prime = sieve()
for i in range(int(input())):
    print(prime[int(input())])

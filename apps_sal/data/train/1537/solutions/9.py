primes = []


def rwh_primes1(n):
    """ Returns  a list of primes < n """
    sieve = [True] * (n // 2)
    for i in range(3, int(n ** 0.5) + 1, 2):
        if sieve[i // 2]:
            sieve[i * i // 2::i] = [False] * ((n - i * i - 1) // (2 * i) + 1)
    return [2] + [2 * i + 1 for i in range(1, n // 2) if sieve[i]]


primes = rwh_primes1(1000000)
plookup = set(primes)
S = []
prime = 10 ** 9 + 7
for i in range(2, 10000):
    if i in plookup:
        S.append(primes[i - 1])


def __starting_point():
    T = int(input())
    while T > 0:
        T -= 1
        N = int(input())
        s = 0
        for i in range(N):
            s += S[i]
        print(s % prime)


__starting_point()

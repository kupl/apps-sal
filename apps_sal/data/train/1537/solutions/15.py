primes = []
for possiblePrime in range(2, 10000):
    isPrime = True
    for num in range(2, int(possiblePrime ** 0.5) + 1):
        if possiblePrime % num == 0:
            isPrime = False
            break
    if isPrime:
        primes.append(possiblePrime)
plookup = set(primes)
S = []
prime = 10 ** 9 + 7
for i in range(2, 1000):
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

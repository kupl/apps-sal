import math


def primeFactors(n):
    primes = {}
    while n % 2 == 0:
        n //= 2
        try:
            primes[2] += 1
        except:
            primes[2] = 1
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            n //= i
            try:
                primes[i] += 1
            except:
                primes[i] = 1
    if n != 1:
        primes[n] = 1
    primes = sorted(list(primes.items()), key=lambda k: k[0])
    return "".join(
        [
            "({}**{})".format(k, v) if v > 1 else "({})".format(k)
            for k, v in primes
        ]
    )

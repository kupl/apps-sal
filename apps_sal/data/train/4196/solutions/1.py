def summationOfPrimes(primes):
    return sum((i for i in range(2, primes + 1) if all((i % j for j in range(2, int(i ** 0.5) + 1)))))

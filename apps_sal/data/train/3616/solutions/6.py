import math


def prime_primes(N):
    primes = [i for i in range(N) if is_prime(i)]
    prime_prms = []
    for i in range(len(primes) - 1):
        for j in range(primes.index(primes[i]) + 1, len(primes)):
            prime_prms.append(primes[i] / primes[j])
    count_of_prime_primes = len(prime_prms)
    return (count_of_prime_primes, math.floor(sum(prime_prms)))


def is_prime(nr):
    if nr > 1:
        for i in range(2, nr):
            if nr % i == 0:
                return False
        return True
    return False

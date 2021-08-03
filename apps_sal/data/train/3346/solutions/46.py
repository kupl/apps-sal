def isprime(num):
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


def gap(g, m, n):
    primes = []
    for x in range(m, n + 1):

        if isprime(x):
            primes.append(x)
        if len(primes) > 1 and primes[len(primes) - 1] - primes[len(primes) - 2] == g:
            return [primes[len(primes) - 2], primes[len(primes) - 1]]

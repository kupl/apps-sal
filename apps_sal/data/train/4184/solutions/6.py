primes = [2, 3, 5, 7]


def gen_prime():
    candidate = primes[-1]
    while True:
        candidate += 2
        if all((candidate % prime != 0 for prime in primes)):
            primes.append(candidate)
            yield candidate


def is_prime(n):
    print(n)
    if n <= 1:
        return False
    if n <= primes[-1]:
        return n in primes
    for prime in primes:
        if n % prime == 0:
            return False
    new_prime = gen_prime()
    while primes[-1] ** 2 < n:
        prime = next(new_prime)
        if n % prime == 0:
            return False
    return True

primes = [2, 3, 5, 7]
setPrimes = set(primes)


def is_prime(n):
    if n <= primes[-1]:
        return n > 1 and n in setPrimes
    limit = int(n**.5)
    for x in primes:
        if x > limit:
            break
        if not n % x:
            return False

    x, delta = primes[-1], 4 if primes[-1] % 6 == 1 else 2
    while x <= limit:
        x, delta = x + delta, 6 - delta
        if is_prime(x):
            primes.append(x)
            setPrimes.add(x)
            if not n % x:
                return False
    return True

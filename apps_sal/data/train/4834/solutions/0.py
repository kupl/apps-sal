def backwardsPrime(start, stop):
    primes = []
    for n in range(start, stop + 1):
        if n not in primes and is_prime(n) and is_prime(reverse(n)) and n != reverse(n):
            primes.append(n)
            if start <= reverse(n) <= stop:
                primes.append(reverse(n))
    return sorted(primes)


def is_prime(n):
    for i in range(2, int(n**(0.5)) + 1):
        if n % i == 0:
            return False
    return True


def reverse(n):
    return int(''.join(str(n)[::-1]))

def prime_digits(num):
    primes = [2, 3, 5, 7]
    while num:
        if num % 10 not in primes:
            return False
        num //= 10
    return True


primes = set([2] + [n for n in range(3, 20000, 2) if all((n % r for r in range(3, int(n ** 0.5) + 1, 2)))])


def not_primes(a, b):
    return [i for i in range(a, b) if prime_digits(i) if i not in primes]

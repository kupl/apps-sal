import math


def is_prime(n):
    return n == 2 or (n > 2 and n % 2 and all((n % i for i in range(3, int(n ** 0.5) + 1, 2))))


def prime_primes(N):
    a = [i for i in range(2, N) if is_prime(i)]
    (total, count) = (0, 0)
    for elem1 in a:
        for elem2 in a:
            if elem1 < elem2:
                count += 1
                total += elem1 / elem2
    return (count, math.floor(total))

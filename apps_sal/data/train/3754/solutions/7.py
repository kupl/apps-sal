from bisect import bisect


def prime_product(n):
    bisect_point = bisect(primes, n // 2)

    # If n is odd then pair must be (2, n - 2) or nothing. This is because 2 is the
    # only even prime and to get an odd number you must add even + odd.
    if n % 2:
        return 2 * (n - 2) if n - 2 in prime_set else 0

    # Check half of prime list (starting from the middle). Return product of first pair found.
    for prime in primes[:bisect_point][::-1]:
        if n - prime in prime_set:
            return prime * (n - prime)

    return 0  # Return 0 if no valid pair found.


def get_primes(n):
    """Sieve of Eratosthenes to calculate all primes less than or equal to n.

    Return set of primes.
    """
    primes = [True] * (n + 1)

    for num in range(2, int(n ** 0.5) + 1):
        if primes[num]:
            primes[num * 2::num] = [False] * len(primes[num * 2::num])

    return [i for i, x in enumerate(primes) if x and i > 1]


# Calculate all primes up to max but only calculate primes once. Then reference master prime list in all test cases.
max_input = 100000
primes = get_primes(max_input)
prime_set = set(primes)

# Using the sqrt function for speed (instead of **0.5)
from math import sqrt


def seiveOfEratosthenes(n):
    # For speed, only grabbing all odd numbers from 3 to SQRT N
    flags = [True for i in range(3, int(sqrt(n)) + 1, 2)]
    # Adding a flag for "2" (effectively a pre-pend here)
    flags.append(True)

    # Iterate through Primes
    prime = 2
    while (prime <= sqrt(n)):
        # Cross Off all multiples of Prime
        for i in range(prime**2, len(flags), prime):
            flags[i] = False

        # Get next Prime
        prime += 1
        while (prime < len(flags) and not flags[prime]):
            prime += 1
    # Get the list of Primes as actual #'s; We need a special case for "2" because it doesn't fit the odds pattern
    if flags[0]:
        primes = [2]
    else:
        primes = []
    primes += [i for i in range(3, len(flags), 2) if flags[i]]

    return primes


def primeFactors(n):
    # Get applicable Prime numbers
    primes = seiveOfEratosthenes(n)
    primes_in_number = []

    for prime in primes:
        # Iterate through each prime, and figure out how many times it goes in
        repeat = 0
        while (not (n % prime)):
            repeat += 1
            n /= prime

        # Add appearing Primes appropriately
        if repeat == 1:
            primes_in_number.append("(" + str(prime) + ")")
        elif repeat:
            primes_in_number.append("(" + str(prime) + "**" + str(repeat) + ")")

    # Only testing primes up to sqrt of n, so we need to add n if it hasn't been reduced to 1
    if n > 1:
        primes_in_number.append("(" + str(int(n)) + ")")

    return ''.join(primes_in_number)

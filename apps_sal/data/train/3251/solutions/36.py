from math import sqrt


def seiveOfEratosthenes(n):
    flags = [True for i in range(3, int(sqrt(n)) + 1, 2)]
    flags.append(True)

    prime = 2
    while (prime <= sqrt(n)):
        for i in range(prime**2, len(flags), prime):
            flags[i] = False

        prime += 1
        while (prime < len(flags) and not flags[prime]):
            prime += 1
    if flags[0]:
        primes = [2]
    else:
        primes = []
    primes += [i for i in range(3, len(flags), 2) if flags[i]]

    return primes


def primeFactors(n):
    primes = seiveOfEratosthenes(n)
    primes_in_number = []

    for prime in primes:
        repeat = 0
        while (not (n % prime)):
            repeat += 1
            n /= prime

        if repeat == 1:
            primes_in_number.append("(" + str(prime) + ")")
        elif repeat:
            primes_in_number.append("(" + str(prime) + "**" + str(repeat) + ")")

    if n > 1:
        primes_in_number.append("(" + str(int(n)) + ")")

    return ''.join(primes_in_number)

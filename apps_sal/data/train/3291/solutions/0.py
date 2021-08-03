def is_prime(n): return all(n % d for d in range(3, int(n ** .5) + 1, 2))


def primes_a_p(lower_limit, upper_limit):
    a_p = []
    for n in range(lower_limit | 1, upper_limit, 2):
        for gap in range(30, (upper_limit - n) // 5 + 1, 30):
            sequence = [n + i * gap for i in range(6)]
            if all(map(is_prime, sequence)):
                a_p.append(sequence)
    return a_p

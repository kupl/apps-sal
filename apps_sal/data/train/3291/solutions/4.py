LIMIT = 10**4
sieve = list(range(LIMIT))
sieve[1] = 0
primes = []
for n in sieve:
    if n:
        primes.append(n)
        for i in range(n * n, LIMIT, n):
            sieve[i] = 0

del sieve
primes.remove(2)


def primes_a_p(lower_limit, upper_limit, k=6):
    primes_list = [p for p in primes if lower_limit <= p <= upper_limit]
    primes_set = set(primes_list)

    max_scope = (upper_limit - lower_limit) // (k - 1)

    base_diff = 2 * 3 * 5

    solutions = []

    for n in range(1, max_scope // base_diff + 1):
        diffs = [n * base_diff * x for x in range(k)]
        scope = n * base_diff * (k - 1)

        for p in primes_list:
            if p + scope > upper_limit:
                break

            if {p + d for d in diffs} <= primes_set:
                solutions.append([p + d for d in diffs])

    return sorted(solutions)

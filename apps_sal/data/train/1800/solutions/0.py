def find_prime_kPerm(n, k):
    sieve = n // 2 * [True]
    for i in range(3, int(n ** .5) + 1, 2):
        if sieve[i // 2]:
            sieve[i*i // 2 :: i] = ((n - i*i - 1) // (2*i) + 1) * [False]
    cycles = {}
    for i in range(1, n // 2):
        if sieve[i]:
            cycles.setdefault(tuple(sorted(str(2*i + 1))), set()).add(2*i + 1)
    k_perms = [min(cycle) for cycle in cycles.values() if len(cycle) == k + 1]
    return [len(k_perms), min(k_perms, default=0), max(k_perms, default=0)]

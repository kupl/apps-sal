def prime_primes(n):
    sieve = [0, 0] + [1] * (n - 2)
    for k in range(2, int(n ** .5) + 1):
        if sieve[k]: sieve[k*k::k] = ((n-k*k-1) // k + 1) * [0]
    primes = [p for p, b in enumerate(sieve) if b]
    ratios = [b / a for i, a in enumerate(primes) for b in primes[:i]]
    return len(ratios), int(sum(ratios))

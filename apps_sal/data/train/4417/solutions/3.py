
def build_solver(limit):
    # Initial list of known values
    reducers = [(2, 0), (3, 0), (5, 0)]
    # Intermediate values known to end in a non-terminating sequence
    known_failures = {2, 3, 5}
    
    def reduces_to_1(p):
        # Determine if successive summation of digit squares reduces to 1
        seq = set()
        n = p
        while n not in seq and n not in known_failures and n != 1:
            seq.add(n)
            m = n
            t = 0
            while m > 0:
                m, d = divmod(m, 10)
                t += d * d
            n = t
        if n != 1:
            # Add to the set of known failing intermeduiate states
            known_failures.update(seq)
        return n == 1
    
    # Build primes up to limit
    prime_candidate = reducers[-1][0]
    root = int(prime_candidate ** 0.5) + 1
    while prime_candidate < limit:
        prime_candidate += 2
        if root * root < prime_candidate:
            root += 1
        for p, _ in reducers:
            if prime_candidate % p == 0:
                break
            if p > root:
                reducers.append((prime_candidate, reduces_to_1(prime_candidate)))
                break
    
    # Keep only those primes that reduce to 1
    reducers = [p for p, r in reducers if r]

    def solve(a, b):
        result = 0
        for p in reducers:
            if p < a:
                continue
            if p >= b:
                break
            result += 1
        return result
    
    return solve
        
solve = build_solver(50_000)

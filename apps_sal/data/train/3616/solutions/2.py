from itertools import combinations

def prime_primes(N):
    primes = [2] + [n for n in range(3, N, 2) if all(n % d for d in range(3, int(n**0.5) + 1, 2))]
    
    pp = [n / float(d) for n, d in combinations(primes, 2)]
    return len(pp), int(sum(pp))
